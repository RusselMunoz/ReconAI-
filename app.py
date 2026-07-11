# app.py
import os
import json
import hashlib
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from dotenv import load_dotenv

# Import our hardcoded demo data
from sample_data import TRANSACTIONS, INVOICES

# Load environment variables
load_dotenv()

app = FastAPI(title="ReconAI MVP")

# Initialize OpenAI client for Fireworks AI
api_key = os.getenv("FIREWORKS_API_KEY")
client = OpenAI(
    api_key=api_key or "dummy_key",
    base_url="https://api.fireworks.ai/inference/v1"
)

def compute_hash_chain(records):
    """
    Computes a SHA-256 hash chain over the combined matched and flagged records.
    Hash of record N = SHA256(JSON_string_of_record_N + hash_of_record_N-1).
    Genesis hash is 64 zeros.
    """
    hash_chain = []
    previous_hash = "0" * 64

    for record in records:
        # Create a deterministic JSON string by sorting keys
        record_json = json.dumps(record, sort_keys=True)
        # Concatenate record JSON with the previous hash
        combined = f"{record_json}{previous_hash}"
        # Compute SHA-256 hash
        current_hash = hashlib.sha256(combined.encode("utf-8")).hexdigest()
        
        # Annotate record with current and previous hash
        annotated_record = {
            **record,
            "hash": current_hash,
            "previous_hash": previous_hash
        }
        hash_chain.append(annotated_record)
        previous_hash = current_hash

    return hash_chain

@app.post("/reconcile")
async def reconcile():
    if not api_key:
        raise HTTPException(status_code=500, detail="FIREWORKS_API_KEY environment variable is not set.")

    # Create the prompt for the Fireworks AI model
    prompt = f"""
    You are an expert bookkeeping assistant. Your task is to reconcile a list of bank transactions against a list of supplier invoices.
    
    Here is the transaction data:
    {json.dumps(TRANSACTIONS, indent=2)}

    Here is the invoice data:
    {json.dumps(INVOICES, indent=2)}

    Please perform the following operations:
    1. MATCH: Pair transactions to invoices where they correspond (same/similar amount, same/close date, matching merchant/supplier name).
       - Provide a confidence score from 0 to 100.
       - Provide a one-sentence reason explaining why it's a match.
    2. FLAG DUPLICATES: Identify duplicate transactions (transactions with different IDs but identical amounts and merchants within 1-2 days).
       - The duplicate transaction should be flagged.
       - The reason should explain which transaction it duplicates.
    3. FLAG MISMATCHES: Identify pairs that correspond but have slight amount discrepancies (e.g. off by a minor transaction fee).
       - Note the exact discrepancy in the reason.
    4. FLAG MISSING INVOICES: Identify transactions that have no corresponding invoice at all (missing documentation).
       - Provide a reason explaining that it lacks documentation.

    Format your output strictly as a JSON object matching this JSON Schema:
    {{
      "matches": [
        {{
          "transaction_id": "string",
          "invoice_id": "string",
          "confidence": 100,
          "reason": "string"
        }}
      ],
      "flags": [
        {{
          "transaction_id": "string",
          "type": "duplicate" or "mismatch" or "missing_invoice",
          "reason": "string"
        }}
      ]
    }}

    Respond ONLY with the JSON object. Do not include any explanation or markdown block wrappers.
    """

    model_name = os.getenv("FIREWORKS_MODEL", "accounts/fireworks/models/glm-5p2")
    try:
        # Request completion from Fireworks AI using the OpenAI-compatible client
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a precise data processing agent. Output ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=4000,
            response_format={"type": "json_object"}
        )
        # Parse the JSON response
        raw_content = response.choices[0].message.content
        result_data = json.loads(raw_content)
        
        matches = result_data.get("matches", [])
        flags = result_data.get("flags", [])

        # Combine matches and flags into a single ordered list of records for the hash chain
        combined_records = []
        for match in matches:
            combined_records.append({
                "record_type": "match",
                "transaction_id": match.get("transaction_id"),
                "invoice_id": match.get("invoice_id"),
                "confidence": match.get("confidence"),
                "reason": match.get("reason")
            })

        for flag in flags:
            combined_records.append({
                "record_type": "flag",
                "transaction_id": flag.get("transaction_id"),
                "type": flag.get("type"),
                "reason": flag.get("reason")
            })

        # Compute the hash chain
        hash_chain = compute_hash_chain(combined_records)

        return {
            "matches": matches,
            "flags": flags,
            "hash_chain": hash_chain
        }

    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse JSON response from Fireworks AI API: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Fireworks AI API: {str(e)}")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")
