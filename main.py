from fastapi import FastAPI
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
