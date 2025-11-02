from transformers import pipeline
import json

ner_model=pipeline("ner",model="dslim/bert-base-NER", aggregation_strategy="simple",grouped_entities=True)
def extract_entities(text:str):
    if not text.strip():
        return {"error": "No text provided for NER extraction."}
    
    # First pass with NER model
    results = ner_model(text)
    
    # Initialize entity dictionary with specific categories
    entity_dict = {
        "PATIENT": "",
        "DOCTOR": "",
        "HOSPITAL": "",
        "DEPARTMENT": "",
        "DATE": "",
        "TIME": "",
        "TOKEN": ""
    }
    
    # Extract basic information using simple pattern matching
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if "Patient Name:" in line:
            entity_dict["PATIENT"] = line.split("Patient Name:")[1].strip()
        elif "Doctor:" in line:
            entity_dict["DOCTOR"] = line.split("Doctor:")[1].strip()
        elif "Department:" in line:
            entity_dict["DEPARTMENT"] = line.split("Department:")[1].strip()
        elif "Date:" in line:
            entity_dict["DATE"] = line.split("Date:")[1].strip()
        elif "Time:" in line:
            entity_dict["TIME"] = line.split("Time:")[1].strip()
        elif "Token No:" in line:
            entity_dict["TOKEN"] = line.split("Token No:")[1].strip()
        elif "CityCare Hospital" in line:
            entity_dict["HOSPITAL"] = "CityCare Hospital"

    return entity_dict
if __name__ == "__main__":
    sample_text = """Barack Obama was born on August 4, 1961, in Honolulu, Hawaii. He served as the 44th President of the United States from 2009 to 2017. Obama graduated from Columbia University and later earned his law degree from Harvard Law School, where he was the first African-American president of the Harvard Law Review."""
    entities = extract_entities(sample_text)
    print(json.dumps(entities, indent=4))