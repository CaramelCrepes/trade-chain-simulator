"""
tests/test_blockchain.py
------------------------
Unit tests for the Blockchain and Block classes.
Run with: python -m pytest tests/
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from blockchain import Block, Blockchain


# ── Block Tests ──────────────────────────────────────

def test_block_has_correct_fields():
    block = Block(index=1, document={"type": "Test"}, previous_hash="0")
    assert block.index == 1
    assert block.document == {"type": "Test"}
    assert block.previous_hash == "0"
    assert block.hash is not None


def test_block_hash_is_deterministic():
    """Same inputs should always produce the same hash."""
    b1 = Block(index=1, document={"type": "Test"}, previous_hash="0")
    b2 = Block.__new__(Block)
    b2.index = b1.index
    b2.timestamp = b1.timestamp
    b2.document = b1.document
    b2.previous_hash = b1.previous_hash
    b2.submitted_by = b1.submitted_by
    assert b1.hash == b2.calculate_hash()


def test_block_hash_changes_when_document_changes():
    """Changing any field should produce a different hash — core of tamper detection."""
    block = Block(index=1, document={"type": "Test", "value": "100"}, previous_hash="0")
    original_hash = block.hash
    block.document["value"] = "999999"  # tamper
    assert block.calculate_hash() != original_hash


def test_block_to_dict_has_all_fields():
    block = Block(index=1, document={"type": "Test"}, previous_hash="0")
    d = block.to_dict()
    assert "index" in d
    assert "timestamp" in d
    assert "document" in d
    assert "previous_hash" in d
    assert "hash" in d
    assert "submitted_by" in d


# ── Blockchain Tests ──────────────────────────────────

def test_blockchain_starts_with_genesis_block():
    bc = Blockchain()
    assert len(bc.chain) == 1
    assert bc.chain[0].document["type"] == "GENESIS"
    assert bc.chain[0].previous_hash == "0"


def test_add_document_increases_chain_length():
    bc = Blockchain()
    bc.add_document({"type": "Bill of Lading", "shipment_id": "SHP-001"})
    assert len(bc.chain) == 2


def test_chain_is_valid_after_adding_documents():
    bc = Blockchain()
    bc.add_document({"type": "Bill of Lading", "shipment_id": "SHP-001"})
    bc.add_document({"type": "Customs Declaration", "shipment_id": "SHP-001"})
    errors = bc.is_valid()
    assert errors == []


def test_chain_detects_hash_tampering():
    """Directly altering a block's document should be detected."""
    bc = Blockchain()
    bc.add_document({"type": "Customs Declaration", "declared_value": "5000"})
    # Tamper directly in memory
    bc.chain[1].document["declared_value"] = "999999"
    errors = bc.is_valid()
    assert len(errors) > 0
    assert any("tampered" in e["message"].lower() or "mismatch" in e["type"].lower() for e in errors)


def test_chain_detects_broken_link():
    """Altering previous_hash should be detected as a broken link."""
    bc = Blockchain()
    bc.add_document({"type": "Bill of Lading"})
    bc.chain[1].previous_hash = "fakehash"
    errors = bc.is_valid()
    assert any("Broken Link" in e["type"] for e in errors)


def test_get_shipment_history_filters_correctly():
    bc = Blockchain()
    bc.add_document({"type": "Bill of Lading", "shipment_id": "SHP-001"})
    bc.add_document({"type": "Bill of Lading", "shipment_id": "SHP-002"})
    bc.add_document({"type": "Customs Declaration", "shipment_id": "SHP-001"})
    history = bc.get_shipment_history("SHP-001")
    assert len(history) == 2
    assert all(b["document"]["shipment_id"] == "SHP-001" for b in history)


def test_get_all_shipment_ids():
    bc = Blockchain()
    bc.add_document({"type": "Bill of Lading", "shipment_id": "SHP-001"})
    bc.add_document({"type": "Bill of Lading", "shipment_id": "SHP-002"})
    ids = bc.get_all_shipment_ids()
    assert "SHP-001" in ids
    assert "SHP-002" in ids
