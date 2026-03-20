# Architecture

## Blockchain Design

Each block is a Python object with these fields:

```
index         → position in the chain
timestamp     → when the block was created
document      → the trade document (dict)
submitted_by  → which user submitted it
previous_hash → hash of the block before this one
hash          → SHA-256 hash of all the above fields
```

## How Hashing Works

When a block is created, all its fields are serialised to a JSON string (with sorted keys for consistency), then hashed with SHA-256:

```python
block_string = json.dumps({...}, sort_keys=True)
hash = hashlib.sha256(block_string.encode()).hexdigest()
```

Any change to any field — even one character — produces a completely different hash.

## How Tamper Detection Works

To validate the chain, we loop through every block and check two things:

1. Recalculate the block's hash from scratch — does it match the stored hash?
2. Does the block's `previous_hash` match the actual hash of the block before it?

If either check fails, the block has been tampered with.

## Why JSON Storage

`ledger.json` is used for simplicity — it makes the tamper demo easy to show (open the file, change a value, reload the app). In a real system this would be a distributed database with multiple nodes.

## Role Enforcement

Routes are protected with a `@login_required(role="exporter")` decorator defined in `auth.py`. The role is stored in Flask's session after login.
