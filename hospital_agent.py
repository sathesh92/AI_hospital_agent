from ocr_reader import extract_text_from_image, extract_text_from_pdf, extract_text
from ner_extract import extract_entities
from llm_reasoner import generating_response

def hospital_agent(file_path: str) -> dict:
    print("/n step 1 :OCR Processing...")
    text_dict = extract_text(file_path)
    if not isinstance(text_dict, dict) or "extracted_text" not in text_dict:
        return {"error": "OCR extraction failed or returned unexpected result."}
    extracted_text = text_dict["extracted_text"]
    if not extracted_text:
        return {"error": "No text found in the provided file."}
    print("Extracted Text:\n", extracted_text)
    print("\n step 2 : NER Processing...")
    fields = extract_entities(extracted_text)
    print("Extracted Entities:\n", fields)
    print("\n step 3 : LLM reasoner...")
    question = "Create a short summary of the patient’s appointment."
    ai_summary = generating_response(fields, question)
    print("Generated Summary:\n", ai_summary)
    return {
        "extracted_text": extracted_text,
        "fields": fields,
        "ai_summary": ai_summary
    }
if __name__ == "__main__":
    test_file_path = r"C:\Users\sathe\Downloads\city_care.pdf"  # Replace with your test file path
    hospital_agent(test_file_path)