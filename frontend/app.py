import streamlit as st
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
