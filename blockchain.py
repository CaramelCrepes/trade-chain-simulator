import hashlib
import json
from datetime import datetime


class Block:
    def __init__(self, index, document, previous_hash, submitted_by="system"):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.document = document
        self.previous_hash = previous_hash
        self.submitted_by = submitted_by
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "document": self.document,
            "previous_hash": self.previous_hash,
            "submitted_by": self.submitted_by
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "document": self.document,
            "previous_hash": self.previous_hash,
            "submitted_by": self.submitted_by,
            "hash": self.hash
        }


class Blockchain:
    LEDGER_FILE = "ledger.json"

    def __init__(self):
        self.chain = []
        self._create_genesis_block()

    def _create_genesis_block(self):
        genesis = Block(
            index=0,
            document={"type": "GENESIS", "message": "TradeChain Simulator — Blockchain Initialised"},
            previous_hash="0",
            submitted_by="system"
        )
        self.chain.append(genesis)

    def add_document(self, document, submitted_by="system"):
        last = self.chain[-1]
        block = Block(
            index=len(self.chain),
            document=document,
            previous_hash=last.hash,
            submitted_by=submitted_by
        )
        self.chain.append(block)
        self.save()
        return block

    def is_valid(self):
        """
        Validates the entire chain.
        Returns list of error dicts — empty means chain is clean.
        """
        errors = []
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            recalculated = curr.calculate_hash()
            if curr.hash != recalculated:
                errors.append({
                    "block": i,
                    "type": "Hash Mismatch",
                    "message": f"Block {i} content has been altered. Stored hash does not match recalculated hash.",
                    "stored": curr.hash[:20] + "...",
                    "expected": recalculated[:20] + "..."
                })

            if curr.previous_hash != prev.hash:
                errors.append({
                    "block": i,
                    "type": "Broken Link",
                    "message": f"Block {i} is not linked to Block {i-1}. Chain integrity broken.",
                    "stored": curr.previous_hash[:20] + "...",
                    "expected": prev.hash[:20] + "..."
                })

        return errors

    def get_shipment_history(self, shipment_id):
        return [
            b.to_dict() for b in self.chain
            if b.document.get("shipment_id") == shipment_id
        ]

    def get_all_shipment_ids(self):
        ids = set()
        for b in self.chain:
            sid = b.document.get("shipment_id")
            if sid:
                ids.add(sid)
        return sorted(ids)

    def simulate_tamper(self):
        """
        Tampers with a real data block for demo purposes.
        Directly edits ledger.json to simulate a real-world attack.
        Returns the index of the tampered block.
        """
        try:
            with open(self.LEDGER_FILE, "r") as f:
                raw = json.load(f)

            # Find the first non-genesis block with a declared_value or amount
            for i in range(1, len(raw)):
                doc = raw[i].get("document", {})
                if "declared_value" in doc:
                    original = doc["declared_value"]
                    doc["declared_value"] = str(int(float(original)) + 999999)
                    raw[i]["document"] = doc
                    with open(self.LEDGER_FILE, "w") as f:
                        json.dump(raw, f, indent=2)
                    return i, "declared_value", original, doc["declared_value"]
                elif "amount" in doc:
                    original = doc["amount"]
                    doc["amount"] = str(int(float(original)) + 999999)
                    raw[i]["document"] = doc
                    with open(self.LEDGER_FILE, "w") as f:
                        json.dump(raw, f, indent=2)
                    return i, "amount", original, doc["amount"]

            return None, None, None, None
        except Exception as e:
            return None, None, None, None

    def restore_from_memory(self):
        """Saves the in-memory chain (untampered) back to disk, restoring integrity."""
        self.save()

    def save(self):
        with open(self.LEDGER_FILE, "w") as f:
            json.dump([b.to_dict() for b in self.chain], f, indent=2)

    def load(self):
        try:
            with open(self.LEDGER_FILE, "r") as f:
                data = json.load(f)
            self.chain = []
            for d in data:
                b = Block.__new__(Block)
                b.index = d["index"]
                b.timestamp = d["timestamp"]
                b.document = d["document"]
                b.previous_hash = d["previous_hash"]
                b.submitted_by = d.get("submitted_by", "system")
                b.hash = d["hash"]
                self.chain.append(b)
        except FileNotFoundError:
            self.chain = []
            self._create_genesis_block()

    def to_list(self):
        return [b.to_dict() for b in self.chain]
