from pathlib import Path
import os

# Base paths
BASE_DIR = Path(__file__).parent
TESSDATA_PREFIX = r"C:\tesseract_data\tessdata"
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# OCR Configuration
OCR_CONFIG = {
    "language": "eng",
    "supported_image_formats": [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"],
    "supported_doc_formats": [".pdf"],
    "pdf_dpi": 300,
    "tesseract_config": "--tessdata-dir {} --dpi 300 --psm 3"
}

# NER Configuration
NER_CONFIG = {
    "model_name": "dslim/bert-base-NER",
    "aggregation_strategy": "simple",
    "field_patterns": {
        "PATIENT": r"Patient Name:\s*(.+)",
        "DOCTOR": r"Doctor:\s*(.+)",
        "HOSPITAL": r"(.+Hospital)",
        "DEPARTMENT": r"Department:\s*(.+)",
        "DATE": r"Date:\s*@?(.+)",
        "TIME": r"Time:\s*(.+)",
        "TOKEN": r"Token No:\s*(\d+)"
    }
}

# LLM Configuration
LLM_CONFIG = {
    "model": "phi3:mini",
    "temperature": 0.7,
    "max_tokens": 150,
    "prompt_template": """
You are an AI hospital assistant.
Your task is to create a summary of the patient's hospital appointment using the extracted entities below.
Use ONLY the provided information - do not add, modify, or substitute any details.

Extracted Information:
{entities}

Write a summary exactly in this format, using only the information provided:
"Patient [PATIENT] has an appointment with [DOCTOR] in the [DEPARTMENT] department on [DATE] at [TIME] at [HOSPITAL]. Token number: [TOKEN]"

IMPORTANT: Use the exact values from the entities, do not make up or substitute any information."""
}

# Error Handling Configuration
ERROR_CONFIG = {
    "max_retries": 3,
    "retry_delay": 1,  # seconds
    "log_level": "INFO",
    "log_file": BASE_DIR / "hospital_agent.log"
}