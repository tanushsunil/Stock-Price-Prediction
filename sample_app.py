import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello world!
""")

st.title("Hello world!")

uploaded_file = st.file_uploader("Upload a harshith")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)
  
  fig, ax = plt.subplots()
  df.hist(
    bins=8,
    column="year",
    row="danceability",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
  st.write(fig)
