import os

# Create folders
os.makedirs("legalEaseAPI", exist_ok=True)
os.makedirs("frontend", exist_ok=True)

# main.py
with open("main.py", "w") as f:
    f.write('''from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LegalEase")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "LegalEase API Running!"}

@app.post("/simplify")
def simplify(data: TextInput):
    # Simple mock - Gemini API connect pannalam
    simplified = f"Simplified: {data.text[:200]}... This document means in simple terms."
    return {"original": data.text, "simplified": simplified}

@app.post("/query")
def query(data: TextInput):
    return {"question": data.text, "answer": "Based on document, this is the answer in simple Tamil/English."}

print("Backend Ready!")
''')

# requirements.txt
with open("requirements.txt", "w") as f:
    f.write("fastapi\nuvicorn\nstreamlit\nrequests\npython-dotenv\n")

# frontend/app.py
with open("frontend/app.py", "w") as f:
    f.write('''import streamlit as st
import requests

st.title("LegalEase - Legal Document Simplifier")
st.write("Upload pannunga, simple-a puriya vekkaren paa!")

text = st.text_area("Legal text inga paste pannunga paa:")

if st.button("Simplify pannu"):
    if text:
        try:
            res = requests.post("http://localhost:8000/simplify", json={"text": text})
            st.success(res.json()["simplified"])
        except:
            st.success(f"Simplified (Demo): {text[:200]} - Ithu simple meaning paa!")
    else:
        st.warning("Text enter pannunga paa!")
''')

print("✅ Project Created Successfully paa!")
print("Files created: main.py, requirements.txt, frontend/app.py")