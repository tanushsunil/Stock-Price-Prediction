import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello world!
""")

dataset = pd.read_csv('./patient_data.csv')

st.line_chart(dataset)
