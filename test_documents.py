"""
tests/test_documents.py
-----------------------
Unit tests for trade document template functions.
Run with: python -m pytest tests/
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from documents import bill_of_lading, certificate_of_origin, customs_declaration, letter_of_credit, shipment_status


def test_bill_of_lading_has_required_fields():
    doc = bill_of_lading("SHP-001", "Tata Exports", "Global Traders",
                          "Electronics", "MV Star", "Mumbai", "Hamburg")
    assert doc["type"] == "Bill of Lading"
    assert doc["shipment_id"] == "SHP-001"
    assert doc["exporter"] == "Tata Exports"
    assert doc["importer"] == "Global Traders"
    assert doc["origin_port"] == "Mumbai"
    assert doc["destination_port"] == "Hamburg"


def test_certificate_of_origin_has_required_fields():
    doc = certificate_of_origin("SHP-001", "Tata Exports", "Electronics", "India", "FICCI")
    assert doc["type"] == "Certificate of Origin"
    assert doc["country_of_origin"] == "India"
    assert doc["issuing_body"] == "FICCI"


def test_customs_declaration_has_required_fields():
    doc = customs_declaration("SHP-001", "Global Traders", "Electronics", "75000", "USD", "8471.30")
    assert doc["type"] == "Customs Declaration"
    assert doc["declared_value"] == "75000"
    assert doc["hs_code"] == "8471.30"


def test_letter_of_credit_has_required_fields():
    doc = letter_of_credit("SHP-001", "Global Traders", "Tata Exports",
                           "75000", "USD", "2024-12-31", "Deutsche Bank")
    assert doc["type"] == "Letter of Credit"
    assert doc["amount"] == "75000"
    assert doc["issuing_bank"] == "Deutsche Bank"


def test_shipment_status_has_required_fields():
    doc = shipment_status("SHP-001", "Mumbai Port", "Departed Port", "On schedule")
    assert doc["type"] == "Status Update"
    assert doc["new_status"] == "Departed Port"
    assert doc["notes"] == "On schedule"


def test_all_documents_have_shipment_id():
    docs = [
        bill_of_lading("SHP-001", "A", "B", "C", "D", "E", "F"),
        certificate_of_origin("SHP-001", "A", "B", "C", "D"),
        customs_declaration("SHP-001", "A", "B", "C", "D", "E"),
        letter_of_credit("SHP-001", "A", "B", "C", "D", "E", "F"),
        shipment_status("SHP-001", "A", "B")
    ]
    for doc in docs:
        assert doc.get("shipment_id") == "SHP-001"
