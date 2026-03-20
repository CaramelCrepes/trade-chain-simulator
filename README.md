# ⬡ TradeChain Simulator

> A blockchain-based trade documentation simulator with role-based dashboards, SHA-256 tamper detection, and a live fraud demo. Built with Python & Flask.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Demo Accounts](#demo-accounts)
- [Role Dashboards](#role-dashboards)
- [Tamper Detection Demo](#tamper-detection-demo)
- [Document Types](#document-types)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

International trade relies on dozens of paper-based documents — Bills of Lading, Letters of Credit, Customs Declarations, and Certificates of Origin. These documents are slow to process, easy to forge, and expensive to verify.

**TradeChain Simulator** demonstrates how blockchain technology can solve this problem by creating a tamper-proof, instantly verifiable digital ledger for trade documents.

Each document is stored as a block in a chain. Every block contains a SHA-256 hash of its own contents plus the hash of the previous block. If anyone alters a document — even changing a single character — the hash chain breaks and the tampering is detected instantly.

This project is inspired by real-world initiatives like **TradeLens** (Maersk + IBM) and the **Marco Polo Network**.

---

## ✨ Features

- 🔐 **SHA-256 blockchain simulation** — every document is hashed and chained
- 👥 **Three role-based dashboards** — Exporter, Importer, Customs Officer
- 📄 **Four document types** — Bill of Lading, Certificate of Origin, Customs Declaration, Letter of Credit
- ⚠️ **Live tamper detection** — simulate a fraud attack and watch the blockchain catch it
- 🔄 **Chain restoration** — restore integrity from in-memory state
- 🗂️ **Shipment history** — track the full document trail for any shipment
- 🌐 **REST API** — JSON endpoints for chain data and verification
- 💾 **Persistent storage** — chain saved to `ledger.json` between sessions

---

## ⚙️ How It Works

```
Exporter submits Bill of Lading
        ↓
Block created with SHA-256 hash of document + previous block's hash
        ↓
Block added to chain → saved to ledger.json
        ↓
Importer files Customs Declaration → another block added
        ↓
Customs Officer verifies entire chain
        ↓
Any tampering → hash mismatch → instantly flagged
```

### Blockchain Structure

Each block contains:
| Field | Description |
|---|---|
| `index` | Block number in the chain |
| `timestamp` | When the block was created |
| `document` | The trade document (dict) |
| `submitted_by` | Which user submitted it |
| `previous_hash` | Hash of the previous block |
| `hash` | SHA-256 hash of this block's contents |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Web Framework | Flask 3.0 |
| Hashing | Python `hashlib` (SHA-256) |
| Storage | JSON flat file (`ledger.json`) |
| Auth | Session-based with `users.json` |
| Frontend | Jinja2 templates + vanilla CSS/JS |

---

## 📁 Project Structure

```
trade-chain-simulator/
│
├── app.py               # Flask routes and role logic
├── blockchain.py        # Block + Blockchain classes, hashing, validation
├── auth.py              # Login, session management, role decorator
├── documents.py         # Trade document templates
├── demo.py              # Seeds blockchain with a sample shipment
├── users.json           # User credentials and roles
├── requirements.txt     # Python dependencies
├── .gitignore
├── LICENSE
│
├── templates/           # Jinja2 HTML templates
│   ├── base.html        # Shared layout and nav
│   ├── login.html       # Login page with demo account quick-fill
│   ├── exporter.html    # Exporter dashboard
│   ├── importer.html    # Importer dashboard
│   ├── customs.html     # Customs officer dashboard + tamper demo
│   └── shipment.html    # Shipment document trail
│
├── docs/                # Documentation
│   ├── ARCHITECTURE.md  # Blockchain design explained
│   ├── ROLES.md         # What each role can do
│   └── API.md           # API endpoint reference
│
├── tests/               # Unit tests
│   ├── test_blockchain.py
│   └── test_documents.py
│
├── examples/            # Sample data
│   ├── sample_block.json
│   └── sample_ledger.json
│
└── screenshots/         # App screenshots
    └── README.md
```

---

## 📋 Prerequisites

- Python 3.10 or higher
- pip

Check your Python version:
```bash
python --version
```

---

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/CaramelCrepes/trade-chain-simulator.git
cd trade-chain-simulator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ⚡ Quick Start

```bash
# Step 1 — seed the blockchain with a sample shipment
python demo.py

# Step 2 — start the web server
python app.py

# Step 3 — open your browser
# http://127.0.0.1:5000
```

---

## 👤 Demo Accounts

Click any account on the login page to auto-fill credentials.

| Username | Password | Role |
|---|---|---|
| `exporter` | `export123` | Exporter |
| `importer` | `import123` | Importer |
| `customs` | `customs123` | Customs Officer |

---

## 🖥️ Role Dashboards

### Exporter
- Submit **Bill of Lading**, **Certificate of Origin**, **Letter of Credit**, **Status Updates**
- View all their own submissions on the blockchain
- Track shipments by ID

### Importer
- View all documents addressed to their company
- File **Customs Declarations** for incoming shipments
- Track shipment history

### Customs Officer
- View the **full blockchain ledger**
- Verify chain integrity in real time
- Issue **customs clearance** blocks
- Run the **tamper detection demo**

---

## 🔴 Tamper Detection Demo

This is the core demonstration of why blockchain matters for trade documentation.

1. Log in as `customs / customs123`
2. Click **⚡ Simulate Tamper Attack**
   - This directly edits `ledger.json` on disk, changing a financial value — simulating a real fraud attack
3. The verification panel immediately shows:
   - Which block was tampered with
   - The stored hash vs the expected hash
   - Exactly what broke in the chain
4. Click **↺ Restore Chain** to recover integrity

This demo shows in 30 seconds why a centralised database can be silently altered, but a blockchain cannot.

---

## 📄 Document Types

| Document | Submitted By | Purpose |
|---|---|---|
| Bill of Lading | Exporter | Proof of shipment — the most important trade document |
| Certificate of Origin | Exporter | Certifies where goods were produced |
| Letter of Credit | Exporter | Bank guarantee of payment |
| Customs Declaration | Importer | Declares goods and value to customs authorities |
| Status Update | Any role | Tracks shipment progress through stages |

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/chain` | Returns the full blockchain as JSON |
| GET | `/api/verify` | Returns chain validity and any errors |
| GET | `/shipment/<id>` | Returns document history for a shipment |

Example response from `/api/verify`:
```json
{
  "valid": true,
  "errors": [],
  "blocks": 7
}
```

---

## 🧪 Running Tests

```bash
python -m pytest tests/
```

Tests cover:
- Block hash calculation
- Chain validation
- Tamper detection
- Document creation

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

1. Fork the repo
2. Create a branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**CaramelCrepes** — 2nd Year Computer Science Student

Built as a portfolio project demonstrating blockchain concepts applied to real-world international trade documentation problems.
