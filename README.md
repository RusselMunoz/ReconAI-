# ReconAI: AI-Powered Reconciliation for Bookkeepers

AI-powered reconciliation using Fireworks.ai on AMD hardware.

## The Problem
* Bookkeepers spend 8-12 hours per week matching transactions across bank statements, invoices, and payment apps.
* Over $5 trillion in B2B payments are reconciled manually each year, which is highly error-prone.
* Approximately 67% of small businesses have accidentally made duplicate payments.
* Existing audit trails are weak, making financial disputes difficult to prove without tamper-evident records.

## The Solution
ReconAI automates the transaction reconciliation workflow by matching bank statements to supplier invoices. The application processes messy data (e.g. amount differences due to transaction fees or offset dates), flags duplicate records, identifies missing documentation, and seals each entry using a cryptographic hash chain to guarantee a tamper-evident audit trail.

## Why AMD + Fireworks AI
* Leverages Fireworks.ai's optimized LLM inference running on AMD GPU hardware.
* Delivers deterministic, high-reasoning bookkeeping matches in under 3 seconds per batch.
* Utilizes AMD Fire Pass credits for developer-accessible, low-cost API inference.

## Quick Start
To run ReconAI locally:
1. Clone this repository.
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your environment variables:
   ```bash
   export FIREWORKS_API_KEY="your_fireworks_api_key"
   ```
4. Start the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```
5. Open `http://localhost:8000` in your web browser.

*Deployed Demo:* [Live Demo URL]

## Demo Script
* **0:00 - 0:10**: Introduce ReconAI and its goal of automated bookkeeping reconciliation on AMD hardware.
* **0:10 - 0:25**: Present the user interface showing the pre-loaded bank transactions and supplier invoices side-by-side.
* **0:25 - 0:45**: Click the "Run Reconciliation" button to trigger the AMD-optimized Fireworks.ai API, showing real-time AI matches, confidence scores, and reasoning flags (e.g., duplicates, mismatches).
* **0:45 - 0:55**: Explain the cryptographic hash chain output that renders the ledger tamper-evident.
* **0:55 - 1:00**: Conclude by showing the performance metrics indicating inference completed in under 3 seconds.

## What's Next
* **File Uploads**: Add CSV and PDF import capability to allow bookkeepers to upload custom bank statements and invoices.
* **Accounting Integrations**: Integrate the QuickBooks Online and Xero APIs to sync transactions automatically.
* **Email Receipt Ingestion**: Build an email inbox ingestion system to match forwarded receipts directly to transactions.
