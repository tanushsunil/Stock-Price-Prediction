import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello world!
""")

dataset = pd.read_csv('./patient_data.csv')
st.title("Hello world!")

uploaded_file = st.file_uploader("Upload a harshith")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(dataframe)
