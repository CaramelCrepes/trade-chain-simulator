# TradeChain Simulator

A role-based blockchain trade documentation simulator built in Python + Flask.

## Quick Start
```bash
pip install flask
python demo.py      # seed sample data
python app.py       # start server → http://127.0.0.1:5000
```

## Demo Accounts
| Username | Password   | Role            |
|----------|------------|-----------------|
| exporter | export123  | Exporter        |
| importer | import123  | Importer        |
| customs  | customs123 | Customs Officer |

## What Each Role Can Do
- **Exporter** — Submit Bill of Lading, Certificate of Origin, Letter of Credit
- **Importer** — View incoming documents, file Customs Declarations
- **Customs** — View full ledger, clear shipments, simulate + detect tampering

## Tamper Detection Demo (the wow moment)
1. Log in as `customs`
2. Click **Simulate Tamper Attack** — alters a financial value in `ledger.json`
3. The verification panel immediately shows which block was compromised
4. Click **Restore Chain** to fix it

## Project Structure
```
trade-sim/
├── blockchain.py     # Block + Blockchain classes
├── documents.py      # Document templates
├── auth.py           # Login + session helpers
├── app.py            # Flask routes
├── users.json        # Credentials (role-based)
├── demo.py           # Seed data
├── ledger.json       # Auto-generated chain
└── templates/        # HTML pages per role
```
