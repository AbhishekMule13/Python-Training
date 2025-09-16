import streamlit as st
import pandas as pd

st.title("Simple Data App")
st.write("Upload a CSV to explore data")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
    st.line_chart(df)
