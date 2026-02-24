import streamlit as st
import os
from utils.chaos import generate_chaos_response
from dotenv import load_dotenv
from utils.sentiment import predict_sentiment

load_dotenv()

st.set_page_config(page_title="AI Playground", layout="wide")
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🧪 AI Playground")

tab1, tab2, tab3 = st.tabs([
    "🔥 Chaos Reactor",
    "😊 Sentiment Analyzer",
    "📊 Data Explorer"
])

with tab1:
    st.markdown("## 🔥 Chaos Reactor")
    st.caption("An emotionally reactive dramatic overreaction engine.")
    st.divider()

    # ---- INIT STATE ----
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chaos_level" not in st.session_state:
        st.session_state.chaos_level = 1

    st.markdown("<br>", unsafe_allow_html=True)
    # ---- SCROLLABLE CHAT ----
    chat_container = st.container(height=400)

    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    # ---- CHAOS INFO + RESET ----
    col1, col2 = st.columns([4, 1])

    with col1:
        st.progress(st.session_state.chaos_level / 10)
        st.caption(f"Chaos Level: {st.session_state.chaos_level} / 10")
    with col2:
        if st.button("Reset"):
            st.session_state.messages = []
            st.session_state.chaos_level = 1
            st.rerun()

    st.divider()

    # ---- CHAT INPUT ----    
    user_input = st.chat_input("Say something ordinary...")

    if user_input:
        # Append user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        sentiment_label, score = predict_sentiment(user_input)

        if sentiment_label == "negative":
            st.session_state.chaos_level += int(score * 3)
        elif sentiment_label == "positive":
            st.session_state.chaos_level -= int(score * 2)
        else:
            st.session_state.chaos_level += 1

        st.session_state.chaos_level = max(
            1, min(10, st.session_state.chaos_level)
        )
        with st.spinner("Chaos intensifying..."):
            response = generate_chaos_response(
                st.session_state.messages,
                st.session_state.chaos_level,
                sentiment_label
            )

        st.session_state.messages.append(
                {"role": "assistant", "content": response}        )

        # Force clean rerun so history re-renders properly
        st.rerun()


with tab2:
    st.header("Sentiment Analyzer")

with tab3:
    st.header("Data Explorer")