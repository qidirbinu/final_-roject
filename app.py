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

with st.expander('visualization'):
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')

#Data preparations
with st.sidebar:
  st.header('input features')
  #"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender',('Male','Female'))
  bill_length_mm = st.slider('Bill length (mm)',32.1,59.6,43.9)

#Create DataFrame for the input value
  data = {'island':island,
          'gender':gender,
          'bill_length_mm':bill_length_mm}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df,X],axis=0)

  #Encode
  encode = ['island','sex']
  df_penguins = pd.get_dummies(input_penguins,prefix=encode)
  input_row = df_penguins[:1]

with st.expander('Input features'):
  st.write('**Input Penguin**')
  input_df
  st.write('**Combined Penguins Data**')
  input_penguins
  #st.write('Encoded input penguins')
  #input_row
 

  
