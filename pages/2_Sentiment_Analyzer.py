import streamlit as st
from utils.sentiment import predict_sentiment

st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

st.title("😊 Sentiment Analyzer")

text = st.text_area("Enter text to analyze:")

if text:
    label, score = predict_sentiment(text)
    st.write(f"**Sentiment:** {label}")
    st.write(f"Confidence: {round(score, 2)}")