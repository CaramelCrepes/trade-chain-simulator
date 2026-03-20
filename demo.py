"""
demo.py — run once to seed the blockchain with a realistic shipment.
Usage: python demo.py
"""
from blockchain import Blockchain
from documents import bill_of_lading, certificate_of_origin, customs_declaration, letter_of_credit, shipment_status

bc = Blockchain()
SID = "SHP-2024-001"
print(f"Seeding shipment {SID}...")

bc.add_document(letter_of_credit(
    shipment_id=SID, applicant="Global Traders GmbH",
    beneficiary="Tata Exports Ltd", amount="75000", currency="USD",
    expiry_date="2024-12-31", issuing_bank="Deutsche Bank"
), submitted_by="exporter")

bc.add_document(bill_of_lading(
    shipment_id=SID, exporter="Tata Exports Ltd", importer="Global Traders GmbH",
    goods="Electronic Components (CPU, RAM, GPU)", vessel="MV Ocean Harmony",
    origin_port="Mumbai", destination_port="Hamburg"
), submitted_by="exporter")

bc.add_document(certificate_of_origin(
    shipment_id=SID, exporter="Tata Exports Ltd", goods="Electronic Components",
    country_of_origin="India", issuing_body="FICCI Mumbai"
), submitted_by="exporter")

bc.add_document(shipment_status(
    shipment_id=SID, updated_by="Tata Exports Ltd",
    new_status="Departed Port", notes="Vessel departed Mumbai on schedule."
), submitted_by="exporter")

bc.add_document(customs_declaration(
    shipment_id=SID, importer="Global Traders GmbH",
    goods="Electronic Components", declared_value="75000",
    currency="USD", hs_code="8471.30"
), submitted_by="importer")

print(f"✓ {len(bc.chain)} blocks created. Chain valid: {len(bc.is_valid()) == 0}")
print("Run: python app.py → open http://127.0.0.1:5000")
