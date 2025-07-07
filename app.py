# app.py
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re

# Load model
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base")
    return tokenizer, model

tokenizer, model = load_model()

# Generate comment
def generate_comment(code):
    input_ids = tokenizer.encode("comment: " + code, return_tensors="pt", truncation=True)
    outputs = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# --- UI Setup ---
st.set_page_config(page_title="Code Comment Generator", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #f4f6fa;
}
.css-18e3th9 {
    padding: 2rem;
    border-radius: 10px;
    background: white;
    box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.08);
}
h1 {
    color: #1f4f7b;
    font-weight: 700;
}
textarea {
    font-family: 'Courier New', monospace;
}
.stButton>button {
    background-color: #1f4f7b;
    color: white;
    font-weight: 600;
    padding: 0.6rem 1.2rem;
    border-radius: 6px;
}
.stButton>button:hover {
    background-color: #163d60;
}
</style>
""", unsafe_allow_html=True)

# --- App Layout ---
st.title("🧠 NLP-Powered Code Comment Generator")
st.subheader("Explain code with AI-powered comments")

code_input = st.text_area("🔣 Paste your code here:", height=200, placeholder="def add(a, b):\n    return a + b")

if st.button("✨ Generate Comment"):
    if not code_input.strip():
        st.warning("Please paste some code.")
    else:
        with st.spinner("Analyzing code..."):
            comment = generate_comment(code_input)
            st.success("✅ Generated Comment:")
            st.code(comment, language="markdown")
