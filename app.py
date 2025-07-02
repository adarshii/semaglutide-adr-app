import streamlit as st
import pandas as pd
import numpy as np

st.title("🧬 Semaglutide ADR Risk Predictor")

uploaded_file = st.file_uploader("📁 Upload Transcriptomics CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Predicting ADR Risk (Mock)")
    risk = np.random.rand() * 100
    st.metric("Predicted ADR Risk", f"{risk:.2f}%")

    st.subheader("🧠 Top Contributing Genes (Simulated)")
    genes = df.columns[1:6]
    scores = np.random.rand(len(genes)) * 100
    for gene, score in zip(genes, scores):
        st.write(f"{gene}: {score:.2f} contribution score")
else:
    st.info("Please upload a file to begin.")

