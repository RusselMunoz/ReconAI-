import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FIREWORKS_API_KEY")
if not api_key:
    print("Error: FIREWORKS_API_KEY not found in environment.")
    exit(1)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.fireworks.ai/inference/v1"
)

try:
    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p6",
        messages=[{"role": "user", "content": 'Output ONLY valid JSON, nothing else. No explanation, no reasoning, no markdown. Just this exact object: {"status": "ok", "message": "test success"}'}],
        response_format={"type": "json_object"},
        temperature=0.0,
        max_tokens=500
    )
    print("Auth Succeeded!")
    print("Raw Response:", response.choices[0].message.content)
except Exception as e:
    print("Auth/Request Failed:", str(e))
