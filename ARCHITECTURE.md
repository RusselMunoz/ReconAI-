# ReconAI Architecture Spec

## System Design
```
┌─────────────────┐             POST /reconcile             ┌─────────────────┐
│     Client      │ ──────────────────────────────────────> │     Backend     │
│ (HTML + CSS/JS) │ <────────────────────────────────────── │ (FastAPI/Python)│
└─────────────────┘             JSON Response               └─────────────────┘
                                                                     │
                                                      HTTPS API Call │
                                                                     ▼
                                                            ┌─────────────────┐
                                                            │  Fireworks.ai   │
                                                            │   (AMD GPUs)    │
                                                            └─────────────────┘
```
ReconAI is built as a lightweight single-page web application. The static client interface talks directly to a FastAPI backend server, which acts as an orchestrator sending prompts to the Fireworks.ai inference engine running on AMD GPUs.

## Data Flow
1. **Trigger**: The user clicks the "Run Reconciliation" button on the client frontend.
2. **Request**: The client sends a `POST` request to `/reconcile` containing the bank transactions and invoices as JSON arrays.
3. **Validation**: The FastAPI backend parses the payload and checks transaction/invoice record types and amounts.
4. **Prompting**: The backend builds a few-shot prompt embedding the input data and requesting a strict JSON schema output.
5. **Inference**: The backend sends the prompt to the Fireworks.ai endpoint using the `mixtral-8x7b-instruct` model.
6. **Parsing**: The backend strips markdown formatting from the response and parses the output matches and flags.
7. **Integrity Sealing**: The backend computes a SHA-256 hash chain over the output records.
8. **Response**: The backend returns the matches, flags, hash chain, and hardware metadata to the client for rendering.

## The Hash Chain
ReconAI secures the reconciliation results against tampering using a sequential SHA-256 hash chain. The hash for each matched record is computed by hashing the concatenated string of the current record's JSON object and the hash of the previous record. This forms an immutable hash chain where any change to past data will break all subsequent hashes. This provides audit-level tampering evidence without the transaction fees, latency, or complexity associated with a blockchain.

## API Specification
### POST `/reconcile`

#### Request JSON Example
```json
{
  "transactions": [
    {
      "id": "tx1",
      "date": "2026-07-01",
      "amount": 123.45,
      "description": "Grocery Store"
    }
  ],
  "invoices": [
    {
      "id": "inv1",
      "date": "2026-07-01",
      "amount": 123.45,
      "supplier": "Grocery Co",
      "ref": "INV-001"
    }
  ]
}
```

#### Response JSON Example
```json
{
  "matches": [
    {
      "tx_id": "tx1",
      "inv_id": "inv1",
      "confidence": 98,
      "reason": "Same amount and date, merchant matches"
    }
  ],
  "flags": [],
  "hash_chain": [
    "a3b5c7d9e1f2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8"
  ],
  "metadata": {
    "model": "mixtral-8x7b-instruct",
    "inference_time_ms": 2847,
    "hardware": "AMD GPU"
  }
}
```

## Tech Stack
| Layer | Technology | AMD Integration |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript | N/A |
| **Backend** | Python, FastAPI | N/A |
| **AI Inference** | Fireworks.ai (Mixtral 8x7B / Llama 2 70B) | AMD GPU-Optimized |
| **Integrity** | SHA-256 hash chaining | N/A |
