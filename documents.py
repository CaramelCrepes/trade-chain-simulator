from datetime import datetime


def bill_of_lading(shipment_id, exporter, importer, goods, vessel, origin_port, destination_port):
    return {
        "type": "Bill of Lading",
        "shipment_id": shipment_id,
        "date_issued": datetime.now().strftime("%Y-%m-%d"),
        "exporter": exporter,
        "importer": importer,
        "goods_description": goods,
        "vessel_name": vessel,
        "origin_port": origin_port,
        "destination_port": destination_port,
        "status": "Issued"
    }


def certificate_of_origin(shipment_id, exporter, goods, country_of_origin, issuing_body):
    return {
        "type": "Certificate of Origin",
        "shipment_id": shipment_id,
        "date_issued": datetime.now().strftime("%Y-%m-%d"),
        "exporter": exporter,
        "goods_description": goods,
        "country_of_origin": country_of_origin,
        "issuing_body": issuing_body,
        "status": "Certified"
    }


def customs_declaration(shipment_id, importer, goods, declared_value, currency, hs_code):
    return {
        "type": "Customs Declaration",
        "shipment_id": shipment_id,
        "date_filed": datetime.now().strftime("%Y-%m-%d"),
        "importer": importer,
        "goods_description": goods,
        "declared_value": declared_value,
        "currency": currency,
        "hs_code": hs_code,
        "status": "Filed"
    }


def letter_of_credit(shipment_id, applicant, beneficiary, amount, currency, expiry_date, issuing_bank):
    return {
        "type": "Letter of Credit",
        "shipment_id": shipment_id,
        "date_issued": datetime.now().strftime("%Y-%m-%d"),
        "applicant": applicant,
        "beneficiary": beneficiary,
        "amount": amount,
        "currency": currency,
        "expiry_date": expiry_date,
        "issuing_bank": issuing_bank,
        "status": "Active"
    }


def shipment_status(shipment_id, updated_by, new_status, notes=""):
    return {
        "type": "Status Update",
        "shipment_id": shipment_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_by": updated_by,
        "new_status": new_status,
        "notes": notes
    }
