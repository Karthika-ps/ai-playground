import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("📊 Data Explorer")

uploaded_file = st.file_uploader("Upload a CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
    st.write("Shape:", df.shape)