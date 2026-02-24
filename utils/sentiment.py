import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

@st.cache_resource
def load_analyzer():
    return SentimentIntensityAnalyzer()

def predict_sentiment(text):
    analyzer = load_analyzer()
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "positive", score
    elif score <= -0.05:
        return "negative", abs(score)
    else:
        return "neutral", abs(score)