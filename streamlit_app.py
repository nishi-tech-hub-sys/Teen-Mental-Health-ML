import streamlit as st
import pandas as pd

st.title("Teen Mental Health Prediction")

st.write("Dataset Preview")

df = pd.read_csv("Teen_Mental_Health_Dataset.csv")
st.dataframe(df.head())
