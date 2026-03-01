import streamlit as st
from utils.style import inject_global_style


# MUST be first Streamlit command
st.set_page_config(page_title="Hybrid Intelligence Lab", layout="wide")
inject_global_style()

st.title("🧠 Hybrid Intelligence Lab")

st.markdown("""
    An interactive system demonstrating how classical NLP,
    stateful logic, and LLM conditioning can work together.

    Explore:
    - 🔥 Emotion Amplification Engine  
    - 😊 Sentiment Analysis Module  
    - 📊 Data Intelligence Toolkit  
    """)
st.markdown("---")
st.caption("Hybrid Intelligence Lab • ML + LLM Demonstration Project")