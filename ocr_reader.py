import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\tesseract_data\tessdata"

def extract_text_from_image(image_path: str) -> str:
    try:
        img = Image.open(image_path)
        return pytesseract.image_to_string(img, lang='eng').strip()
    except Exception as e:
        print(f"Error processing image file: {e}")
        return ""

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        pages = convert_from_path(pdf_path)
        return " ".join(pytesseract.image_to_string(p, lang='eng').strip() for p in pages)
    except Exception as e:
        print(f"Error processing PDF file: {e}")
        return ""
def extract_text(file_path: str) -> dict:
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']:
        text = extract_text_from_image(file_path)
    elif ext == '.pdf':
        text = extract_text_from_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    return {"extracted_text": text}
if __name__ == "__main__":
    test_image_path = "sample_image.png"
    test_pdf_path = r"C:\Users\sathe\Downloads\Compensation_560532_2025-2026.pdf"

    
    print("\nExtracted text from PDF:")
    print(extract_text(test_pdf_path))