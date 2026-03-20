# Role Guide

## Exporter (username: exporter)

The exporter initiates a shipment and submits the key documents.

**Can submit:**
- Bill of Lading — issued when goods are handed to the carrier
- Certificate of Origin — proves where goods were manufactured
- Letter of Credit — bank-backed payment guarantee
- Status Updates — e.g. "Goods Ready", "Departed Port"

**Can view:**
- Their own submissions only

**Real-world equivalent:** A company like Tata Exports Ltd shipping goods overseas.

---

## Importer (username: importer)

The importer receives the shipment and handles customs on their end.

**Can submit:**
- Customs Declaration — declares goods and value to customs authorities

**Can view:**
- All documents addressed to their company
- Full shipment history for any shipment ID

**Real-world equivalent:** A company like Global Traders GmbH receiving imported goods.

---

## Customs Officer (username: customs)

The customs officer is the authority that verifies everything.

**Can do:**
- View the full blockchain ledger (all blocks)
- Verify chain integrity at any time
- Issue customs clearance for a shipment
- Run the tamper detection demo
- Restore the chain after a tamper simulation

**Real-world equivalent:** Hamburg Customs Authority or any national customs body.
