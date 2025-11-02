
import re
from config import NER_CONFIG

def extract_entities(text: str):
    if not text or not text.strip():
        return {"error": "No text provided for NER extraction."}

    patterns = NER_CONFIG.get("field_patterns", {})
    entity_dict = {key: "" for key in patterns.keys()}

    # Extract using regex patterns
    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            entity_dict[field] = match.group(1).strip()

    # Fallbacks for conversational input
    # Patient name from "my name is ..." or "hey my name is ..."
    if not entity_dict["PATIENT"]:
        m = re.search(r"my name is ([A-Za-z .'-]+)", text, re.IGNORECASE)
        if m:
            entity_dict["PATIENT"] = m.group(1).strip()

    # Doctor from "with Dr. ..." or "Dr. ..."
    if not entity_dict["DOCTOR"]:
        m = re.search(r"with (Dr\.? [A-Za-z .'-]+)", text, re.IGNORECASE)
        if m:
            entity_dict["DOCTOR"] = m.group(1).strip()
        else:
            m = re.search(r"Dr\.? ?[A-Za-z .'-]+", text, re.IGNORECASE)
            if m:
                entity_dict["DOCTOR"] = m.group(0).strip()

    # Date from "on date:..." or "on ..."
    if not entity_dict["DATE"]:
        m = re.search(r"on date:?\s*([0-9a-zA-Z ,'-]+)", text, re.IGNORECASE)
        if m:
            entity_dict["DATE"] = m.group(1).strip()
        else:
            m = re.search(r"on ([0-9]{1,2}(st|nd|rd|th)? [A-Za-z]+)", text, re.IGNORECASE)
            if m:
                entity_dict["DATE"] = m.group(1).strip()

    # Hospital from "in ... hospital" or "at ... hospital"
    if not entity_dict["HOSPITAL"]:
        m = re.search(r"(?:in|at) ([A-Za-z0-9 .,&'-]+Hospital)", text, re.IGNORECASE)
        if m:
            entity_dict["HOSPITAL"] = m.group(1).strip()
        else:
            hospital_match = re.search(r"([A-Za-z0-9 .,&'-]+Hospital)", text, re.IGNORECASE)
            if hospital_match:
                entity_dict["HOSPITAL"] = hospital_match.group(1).strip()

    # Department from "in the ... department" or "ENT (Ear, Nose & Throat) department"
    if not entity_dict["DEPARTMENT"]:
        m = re.search(r"in the ([A-Za-z0-9 ()&,'-]+) department", text, re.IGNORECASE)
        if m:
            entity_dict["DEPARTMENT"] = m.group(1).strip()
        else:
            m = re.search(r"([A-Za-z0-9 ()&,'-]+) department", text, re.IGNORECASE)
            if m:
                entity_dict["DEPARTMENT"] = m.group(1).strip()

    # Time from "at [time]" (if not a hospital)
    if not entity_dict["TIME"]:
        m = re.search(r"at ([0-9]{1,2}(:[0-9]{2})? ?[ap]m)", text, re.IGNORECASE)
        if m:
            entity_dict["TIME"] = m.group(1).strip()

    # Token fallback: look for "Token number: ..." or "Token: ..."
    if not entity_dict["TOKEN"]:
        m = re.search(r"Token (?:number|no)?[: ]+([0-9]+)", text, re.IGNORECASE)
        if m:
            entity_dict["TOKEN"] = m.group(1).strip()

    return entity_dict
if __name__ == "__main__":
    import json
    sample_text = """
CityCare Hospital
Patient Name: Sathesh Kumar
Doctor: Dr. Meena
Department: Cardiology
Date: 02-Nov-2025
Time: 10:30 AM
Token No: 14
"""
    entities = extract_entities(sample_text)
    print(json.dumps(entities, indent=4))