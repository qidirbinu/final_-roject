import streamlit as st
import pandas as pd
st.title('Machine learning app')

st.info('this is machine learning model')
df=pd.read_csv('https://raw.githubusercontent.com/qidirbinu/latihan/refs/heads/main/penguins_cleaned.csv')
df
