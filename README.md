🏥 AI Hospital Appointment Assistant
🧠 Project Overview

This project is part of my AI Friday learning journey at TCS —
where I set out to build a real-world AI Agent for Intelligent Back-Office Document Processing.

The goal was to create an AI assistant that can automatically:

Read scanned or digital hospital appointment forms (PDF/Image)

Extract key fields such as Patient Name, Doctor, Department, Date, Time, Token No.

Generate a natural language summary using an LLM Reasoner

Present everything inside a clean Streamlit web app

This project represents a complete AI pipeline — from raw document → structured data → human-like explanation.

🧩 Learning Journey — Step by Step
🪄 1. OCR (Optical Character Recognition)

Learned how to extract text from scanned PDFs and images using:

pytesseract

pdf2image

Pillow

Faced multiple setup challenges (Tesseract path, Poppler dependency) and solved them step-by-step.

Validated extraction accuracy using real hospital documents.

🧠 2. NER (Named Entity Recognition)

Initially used a pretrained Hugging Face model: dslim/bert-base-NER

Learned about subword tokens (##) and BERT special tokens ([CLS], [SEP])

Later switched to regex + pattern-based field extraction for higher accuracy on structured hospital forms

Added domain-specific categories: Patient, Doctor, Department, Hospital, Date, Time, Token

💬 3. LLM Reasoning (Ollama + Phi3-mini)

Integrated Ollama local LLM (phi3:mini) for text reasoning

Designed prompt engineering to:

Prevent hallucination

Use only extracted data

Write human-like summaries

Tuned temperature and prompt structure for factual, concise responses.

⚙️ 4. Agent Orchestration

Combined OCR → NER → Reasoner using hospital_agent.py

Built robust error handling (fallback to NER if fields missing)

Structured the output as:

{
  "Hospital": "CityCare Hospital",
  "Patient": "Sathesh Kumar",
  "Doctor": "Dr. Meena",
  "Department": "Cardiology",
  "Date": "02-Nov-2025",
  "Time": "10:30 AM",
  "Token": "14"
}

🌐 5. Streamlit Frontend

Designed an interactive UI using Streamlit

Users can upload PDF or image files, view extracted data, and download structured output as JSON

Added icons, sections, and expanders for a professional layout

🧰 Tech Stack
Component	Library / Tool	Purpose
Language	Python 3.11+	Core programming
OCR	pytesseract, pdf2image, Pillow	Text extraction
NER / Parsing	Regex, Hugging Face Transformers	Field extraction
LLM Reasoner	Ollama (phi3:mini)	Natural language summary
Frontend	Streamlit	Interactive web app
Other Tools	Poppler, Tesseract OCR Engine	PDF/Image processing
🚀 How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/yourusername/ai-hospital-agent.git
cd ai-hospital-agent

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # for Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run app_frontend.py

5️⃣ Upload a Hospital Form (PDF or Image)

✅ The app will automatically:

Extract text (OCR)

Parse fields (regex / NER)

Generate summary (LLM)

Display structured results + allow download

🧾 Example Output

Input PDF:

CityCare Hospital
Patient Name: Sathesh Kumar
Doctor: Dr. Meena
Department: Cardiology
Date: 02-Nov-2025
Time: 10:30 AM
Token No: 14


AI Output:

{
  "Hospital": "CityCare Hospital",
  "Patient": "Sathesh Kumar",
  "Doctor": "Dr. Meena",
  "Department": "Cardiology",
  "Date": "02-Nov-2025",
  "Time": "10:30 AM",
  "Token": "14"
}


AI Summary:

“Patient Sathesh Kumar has an appointment with Dr. Meena in the Cardiology department on 02-Nov-2025 at 10:30 AM at CityCare Hospital.”

🧭 Learnings and Key Takeaways

Understood the complete AI document pipeline (OCR → NLP → Reasoning → UI)

Gained hands-on experience with Tesseract, Poppler, and Ollama LLM

Learned prompt engineering and safe data handling (no fabricated info)

Built modular, production-grade code using Python and Streamlit

Experienced real debugging: environment variables, Unicode errors, and dependency setup

Developed confidence to adapt the same structure to other domains:

Invoice Processing

Purchase Orders

HR Forms

Insurance Claims

🏁 Future Enhancements

Add support for multiple pages & batch uploads

Integrate with FastAPI backend for enterprise deployment

Include PDF report generation with extracted summary

Use CrewAI or LangChain for multi-agent coordination

Add fine-tuned local LLM for healthcare-specific summarization

💬 Acknowledgment

This project was built as part of my TCS AI Friday Learning Challenge,
where the goal is to apply AI to automate manual document workflows.
Special thanks to mentors, teammates, and GitHub AI tools that supported the development process. 🙌

👨‍💻 Author

Sathesh Kumar P
Python | OCR | LLM | Streamlit | AI Automation