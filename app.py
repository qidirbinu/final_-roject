import streamlit as st
import pandas as pd
st.title('Machine learning app')

st.info('this is machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/qidirbinu/latihan/refs/heads/main/penguins_cleaned.csv')
  df

  st.write('**X**')
  X=df.drop('species', axis=1)
  X

  st.write('**y**')
  y=df.species
  y
