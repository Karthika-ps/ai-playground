import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.sentiment import predict_sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from utils.style import apply_global_style

st.set_page_config(page_title="Sentiment Analysis Engine", layout="wide")
apply_global_style()

st.markdown("## 😊 Sentiment Analysis Engine")
st.caption("Lexicon-based polarity detection using VADER.")

text = st.text_area("Enter text to analyze:", height=150)

if text:

    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)

    label, compound_score = predict_sentiment(text)

    st.markdown(f"### 🧠 Detected Sentiment: **{label.upper()}**")
    st.markdown(f"**Compound Score:** {round(compound_score, 3)}")

    st.divider()

    # --- Polarity Breakdown Chart ---
    st.markdown("### 📊 Polarity Breakdown")

    df = pd.DataFrame({
        "Category": ["Negative", "Neutral", "Positive"],
        "Score": [scores["neg"], scores["neu"], scores["pos"]]
    })

    fig, ax = plt.subplots()
    ax.bar(df["Category"], df["Score"])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Score")
    ax.set_title("Sentiment Polarity Distribution")

    st.pyplot(fig)

    st.divider()

    # --- Compound Score Gauge ---
    st.markdown("### 🎯 Emotional Polarity Gauge")

    st.progress((compound_score + 1) / 2)

    if compound_score >= 0.05:
        st.success("Overall tone is Positive.")
    elif compound_score <= -0.05:
        st.error("Overall tone is Negative.")
    else:
        st.info("Overall tone is Neutral.")
    result_data = pd.DataFrame({
        "Text": [text],
        "Sentiment": [label],
        "Compound Score": [compound_score]
    })

    st.download_button(
        label="⬇ Download Sentiment Result",
        data=result_data.to_csv(index=False),
        file_name="sentiment_result.csv",
        mime="text/csv"
    )
