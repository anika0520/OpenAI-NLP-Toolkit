# app.py
import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# Helper function to call GPT
# -----------------------------
def chat_with_ai(role, prompt, temperature=0.4, tokens=400):
    """Generic function to interact with GPT-4/3.5 via OpenAI API"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # can switch to gpt-3.5-turbo if needed
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=tokens
    )
    return response.choices[0].message.content.strip()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Code & Content Generator", page_icon="🤖", layout="centered")
st.title("🤖 AI Code & Content Generator")
st.caption("Powered by OpenAI | Created by Anika")

# Sidebar options
option = st.sidebar.selectbox(
    "Choose a Task",
    [
        "Generate EDA Code",
        "Generate Visualization Code",
        "Generate Resume Summary",
        "Generate Interview Questions",
        "Generate Meeting Summary"
    ]
)

# -----------------------------
# EDA Code Generator
# -----------------------------
if option == "Generate EDA Code":
    st.subheader("📊 Exploratory Data Analysis (EDA)")
    if st.button("Generate EDA Code"):
        with st.spinner("Generating EDA code..."):
            result = chat_with_ai(
                "You are a Python expert.",
                "Write clean, well-commented Python code for Exploratory Data Analysis (EDA) using pandas and matplotlib."
            )
            st.code(result, language="python")

# -----------------------------
# Visualization Code Generator
# -----------------------------
elif option == "Generate Visualization Code":
    st.subheader("📈 Data Visualization Code")
    if st.button("Generate Visualization Code"):
        with st.spinner("Generating visualization code..."):
            result = chat_with_ai(
                "You are a Data Visualization expert.",
                "Generate Python code for data visualization using matplotlib and seaborn on a sample dataset. Include labeled plots and comments."
            )
            st.code(result, language="python")

# -----------------------------
# Resume Summary Generator
# -----------------------------
elif option == "Generate Resume Summary":
    st.subheader("🧠 Resume Summary Generator")
    paragraph = st.text_area("Enter your experience or skillset paragraph:")
    if st.button("Generate Summary"):
        with st.spinner("Creating professional summary..."):
            result = chat_with_ai(
                "You are a resume writing assistant.",
                f"Create a professional, ATS-friendly resume summary for a student or developer based on this:\n{paragraph}"
            )
            st.success("✨ Generated Resume Summary:")
            st.write(result)

# -----------------------------
# Interview Questions Generator
# -----------------------------
elif option == "Generate Interview Questions":
    st.subheader("💻 Interview Question Generator")
    lang = st.text_input("Enter a programming language:", "Python")
    if st.button("Generate Questions"):
        with st.spinner(f"Generating {lang} interview questions..."):
            result = chat_with_ai(
                "You are a technical interviewer.",
                f"Generate 10 technical interview questions for {lang}, mixing theory and coding-based ones."
            )
            st.write(result)

# -----------------------------
# Meeting Summary Generator
# -----------------------------
elif option == "Generate Meeting Summary":
    st.subheader("📋 Meeting Summary Generator")
    notes = st.text_area("Paste meeting notes below:")
    if st.button("Summarize Notes"):
        with st.spinner("Summarizing meeting notes..."):
            result = chat_with_ai(
                "You are a professional meeting summarizer.",
                f"Summarize these meeting notes into 5 concise bullet points:\n{notes}"
            )
            st.success("📝 Meeting Summary:")
            st.write(result)
