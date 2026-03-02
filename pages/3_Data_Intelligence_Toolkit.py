import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.style import apply_global_style

st.set_page_config(page_title="Data Intelligence Toolkit", layout="wide")
apply_global_style()

st.markdown("## 📊 Data Intelligence Toolkit")
st.caption("Interactive dataset inspection and visualization.")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### 🔍 Dataset Preview")
    st.download_button(
        label="⬇ Download Dataset as CSV",
        data=df.to_csv(index=False),
        file_name="processed_data.csv",
        mime="text/csv"
                    )
    st.dataframe(df.head())

    st.markdown("### 📐 Dataset Info")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    with col2:
        missing = df.isnull().sum().sum()
        st.write("Total Missing Values:", missing)

    st.divider()

    st.markdown("### 📈 Visualization")

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if numeric_cols:
        selected_col = st.selectbox("Select numeric column to visualize", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected_col].dropna(), bins=20)
        ax.set_title(f"Distribution of {selected_col}")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequency")

        st.pyplot(fig)

    else:
        st.warning("No numeric columns available for visualization.")
