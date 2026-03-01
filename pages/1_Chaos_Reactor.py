import streamlit as st
from utils.chaos import generate_chaos_response
from utils.sentiment import predict_sentiment

st.set_page_config(page_title="Chaos Reactor", layout="wide")

st.title("🔥 Chaos Reactor")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chaos_level" not in st.session_state:
    st.session_state.chaos_level = 1

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Say something ordinary...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    sentiment_label, score = predict_sentiment(user_input)

    if sentiment_label == "negative":
        st.session_state.chaos_level += max(1, int(score * 2))
    elif sentiment_label == "positive":
        st.session_state.chaos_level -= max(1, int(score * 2))
    else:
        st.session_state.chaos_level += 1

    st.session_state.chaos_level = max(1, min(10, st.session_state.chaos_level))

    response = generate_chaos_response(
        st.session_state.messages,
        st.session_state.chaos_level,
        sentiment_label
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()