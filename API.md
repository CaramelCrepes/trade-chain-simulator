# API Reference

Base URL: `http://127.0.0.1:5000`

---

## GET /api/chain

Returns the full blockchain as a JSON array.

**Response:**
```json
[
  {
    "index": 0,
    "timestamp": "2024-03-01 10:00:00",
    "document": { "type": "GENESIS", "message": "TradeChain Simulator initialised" },
    "submitted_by": "system",
    "previous_hash": "0",
    "hash": "abc123..."
  },
  {
    "index": 1,
    "timestamp": "2024-03-01 10:01:00",
    "document": {
      "type": "Bill of Lading",
      "shipment_id": "SHP-2024-001",
      "exporter": "Tata Exports Ltd",
      "importer": "Global Traders GmbH",
      "goods_description": "Electronic Components",
      "vessel_name": "MV Ocean Harmony",
      "origin_port": "Mumbai",
      "destination_port": "Hamburg",
      "status": "Issued"
    },
    "submitted_by": "exporter",
    "previous_hash": "abc123...",
    "hash": "def456..."
  }
]
```

---

## GET /api/verify

Returns the validity of the entire chain.

**Response (valid chain):**
```json
{
  "valid": true,
  "errors": [],
  "blocks": 7
}
```

**Response (tampered chain):**
```json
{
  "valid": false,
  "errors": [
    {
      "block": 3,
      "type": "Hash Mismatch",
      "message": "Block 3 content has been altered.",
      "stored": "abc123...",
      "expected": "xyz789..."
    }
  ],
  "blocks": 7
}
```

---

## GET /shipment/<shipment_id>

Returns all blocks related to a specific shipment ID.

**Example:** `/shipment/SHP-2024-001`
