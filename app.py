# app_frontend.py
import streamlit as st
import os
from hospital_agent import hospital_agent

st.set_page_config(page_title="🏥 AI Hospital Appointment Assistant", page_icon="💉", layout="wide")

# ---------- HEADER ----------
st.title("🏥 AI Hospital Appointment Assistant")
st.write("Upload a hospital form (PDF or Image) and let the AI extract all details automatically.")

# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("📂 Upload Hospital Form", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    temp_path = os.path.join("temp_input." + uploaded_file.name.split(".")[-1])
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Debug info: file size and type
    file_size = os.path.getsize(temp_path)
    st.info(f"✅ File uploaded successfully! File size: {file_size} bytes. Type: {uploaded_file.type}")
    if file_size == 0:
        st.error("Uploaded file is empty or corrupted. Please upload a valid PDF or image.")
    else:
        with st.spinner("🤖 Running AI pipeline... please wait ⏳"):
            try:
                result = hospital_agent(temp_path)
            except Exception as e:
                st.error(f"⚠️ Error processing file: {e}")
                result = None

        if result:
            # ---------- RESULTS DISPLAY ----------
            if "error" in result:
                st.error(result["error"])
            else:
                st.success("🎉 AI Processing Complete!")
                with st.expander("📜 Extracted Text (from OCR)", expanded=False):
                    st.text(result["extracted_text"])
                with st.expander("🧠 Extracted Fields (Structured Data)", expanded=True):
                    st.json(result["fields"])
                st.markdown("---")
                st.subheader("🤖 AI Summary")
                st.write(result["ai_summary"])
                # Optional: download structured data
                import json
                st.download_button(
                    label="📥 Download Extracted Data (JSON)",
                    data=json.dumps(result["fields"], indent=2),
                    file_name="hospital_data.json",
                    mime="application/json"
                )

else:
    st.warning("Please upload a PDF or image file to continue.")

# Footer
st.markdown("---")
st.markdown("**Developed by Sathesh Kumar — TCS AI Friday Project 🚀**")