from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from blockchain import Blockchain
from documents import bill_of_lading, certificate_of_origin, customs_declaration, letter_of_credit, shipment_status
from auth import authenticate, login_required, current_user

app = Flask(__name__)
app.secret_key = "tradechainsimsecret2024"

# Global blockchain instance — loaded once at startup
bc = Blockchain()
bc.load()

# ──────────────────────────────────────────────────────
# AUTH
# ──────────────────────────────────────────────────────

@app.route("/", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        user = authenticate(username, password)
        if user:
            session["user"] = user
            flash(f"Welcome back, {user['name']}!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required()
def dashboard():
    user = current_user()
    role = user["role"]
    if role == "exporter":
        return redirect(url_for("exporter_dashboard"))
    elif role == "importer":
        return redirect(url_for("importer_dashboard"))
    elif role == "customs":
        return redirect(url_for("customs_dashboard"))
    return redirect(url_for("login"))


# ──────────────────────────────────────────────────────
# EXPORTER DASHBOARD
# ──────────────────────────────────────────────────────

@app.route("/exporter")
@login_required(role="exporter")
def exporter_dashboard():
    user = current_user()
    # Show only shipments this exporter submitted
    my_blocks = [
        b for b in bc.to_list()
        if b["submitted_by"] == user["username"] and b["document"]["type"] != "GENESIS"
    ]
    shipment_ids = bc.get_all_shipment_ids()
    return render_template("exporter.html", user=user, blocks=my_blocks, shipment_ids=shipment_ids)


@app.route("/exporter/submit", methods=["POST"])
@login_required(role="exporter")
def exporter_submit():
    user = current_user()
    doc_type = request.form.get("doc_type")
    shipment_id = request.form.get("shipment_id", "").strip()

    if not shipment_id:
        flash("Shipment ID is required.", "error")
        return redirect(url_for("exporter_dashboard"))

    if doc_type == "Bill of Lading":
        doc = bill_of_lading(
            shipment_id=shipment_id,
            exporter=user["company"],
            importer=request.form.get("importer"),
            goods=request.form.get("goods"),
            vessel=request.form.get("vessel"),
            origin_port=request.form.get("origin_port"),
            destination_port=request.form.get("destination_port")
        )
    elif doc_type == "Certificate of Origin":
        doc = certificate_of_origin(
            shipment_id=shipment_id,
            exporter=user["company"],
            goods=request.form.get("goods"),
            country_of_origin=user["country"],
            issuing_body=request.form.get("issuing_body")
        )
    elif doc_type == "Letter of Credit":
        doc = letter_of_credit(
            shipment_id=shipment_id,
            applicant=request.form.get("applicant"),
            beneficiary=user["company"],
            amount=request.form.get("amount"),
            currency=request.form.get("currency", "USD"),
            expiry_date=request.form.get("expiry_date"),
            issuing_bank=request.form.get("issuing_bank")
        )
    elif doc_type == "Status Update":
        doc = shipment_status(
            shipment_id=shipment_id,
            updated_by=user["company"],
            new_status=request.form.get("new_status"),
            notes=request.form.get("notes", "")
        )
    else:
        flash("Unknown document type.", "error")
        return redirect(url_for("exporter_dashboard"))

    block = bc.add_document(doc, submitted_by=user["username"])
    flash(f"'{doc_type}' added to blockchain as Block #{block.index}.", "success")
    return redirect(url_for("exporter_dashboard"))


# ──────────────────────────────────────────────────────
# IMPORTER DASHBOARD
# ──────────────────────────────────────────────────────

@app.route("/importer")
@login_required(role="importer")
def importer_dashboard():
    user = current_user()
    shipment_ids = bc.get_all_shipment_ids()
    # Show all blocks relevant to the importer's company
    my_blocks = [
        b for b in bc.to_list()
        if b["document"].get("importer") == user["company"]
        or b["document"].get("applicant") == user["company"]
        or b["submitted_by"] == user["username"]
    ]
    return render_template("importer.html", user=user, blocks=my_blocks, shipment_ids=shipment_ids)


@app.route("/importer/submit", methods=["POST"])
@login_required(role="importer")
def importer_submit():
    user = current_user()
    shipment_id = request.form.get("shipment_id", "").strip()

    doc = customs_declaration(
        shipment_id=shipment_id,
        importer=user["company"],
        goods=request.form.get("goods"),
        declared_value=request.form.get("declared_value"),
        currency=request.form.get("currency", "USD"),
        hs_code=request.form.get("hs_code")
    )

    block = bc.add_document(doc, submitted_by=user["username"])
    flash(f"Customs Declaration submitted as Block #{block.index}.", "success")
    return redirect(url_for("importer_dashboard"))


# ──────────────────────────────────────────────────────
# CUSTOMS OFFICER DASHBOARD
# ──────────────────────────────────────────────────────

@app.route("/customs")
@login_required(role="customs")
def customs_dashboard():
    user = current_user()
    chain = bc.to_list()
    errors = bc.is_valid()
    shipment_ids = bc.get_all_shipment_ids()
    return render_template(
        "customs.html",
        user=user,
        chain=chain,
        errors=errors,
        shipment_ids=shipment_ids,
        chain_length=len(bc.chain)
    )


@app.route("/customs/clear", methods=["POST"])
@login_required(role="customs")
def customs_clear():
    user = current_user()
    shipment_id = request.form.get("shipment_id")
    doc = shipment_status(
        shipment_id=shipment_id,
        updated_by=user["company"],
        new_status="Customs Cleared",
        notes="All documents verified. Shipment approved for delivery."
    )
    block = bc.add_document(doc, submitted_by=user["username"])
    flash(f"Shipment {shipment_id} cleared by customs — Block #{block.index} added.", "success")
    return redirect(url_for("customs_dashboard"))


@app.route("/customs/tamper", methods=["POST"])
@login_required(role="customs")
def simulate_tamper():
    """Demo: tampers with ledger.json on disk to simulate a fraud attack."""
    block_i, field, original, faked = bc.simulate_tamper()
    if block_i:
        flash(
            f"⚠ TAMPER SIMULATED — Block #{block_i}: '{field}' changed from {original} to {faked}. "
            f"Run verification to detect it.",
            "tamper"
        )
    else:
        flash("Could not find a suitable block to tamper with.", "error")
    return redirect(url_for("customs_dashboard"))


@app.route("/customs/restore", methods=["POST"])
@login_required(role="customs")
def restore_chain():
    """Restores the chain from in-memory state (untampered) back to disk."""
    bc.restore_from_memory()
    flash("✓ Chain restored from memory. Integrity recovered.", "success")
    return redirect(url_for("customs_dashboard"))


# ──────────────────────────────────────────────────────
# SHARED — SHIPMENT DETAIL
# ──────────────────────────────────────────────────────

@app.route("/shipment/<shipment_id>")
@login_required()
def shipment_detail(shipment_id):
    user = current_user()
    history = bc.get_shipment_history(shipment_id)
    return render_template("shipment.html", user=user, shipment_id=shipment_id, history=history)


# ──────────────────────────────────────────────────────
# API
# ──────────────────────────────────────────────────────

@app.route("/api/verify")
def api_verify():
    errors = bc.is_valid()
    return jsonify({"valid": len(errors) == 0, "errors": errors, "blocks": len(bc.chain)})


@app.route("/api/chain")
def api_chain():
    return jsonify(bc.to_list())


if __name__ == "__main__":
    app.run(debug=True)
