import streamlit as st

def inject_global_style():
    st.markdown("""
    <style>

    /* ---------- Typography ---------- */

    h1 {
        letter-spacing: -1px;
    }

    h1, h2, h3 {
        font-weight: 600;
    }

    /* ---------- Sidebar ---------- */

    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }


    </style>
    """, unsafe_allow_html=True)