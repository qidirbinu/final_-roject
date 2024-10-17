import streamlit as st
import joblib
import numpy as np

# Muat model
model = joblib.load('bullying_model.pkl')

# Definisikan fungsi untuk prediksi
def predict_bullying(text):
    # Tambahkan langkah preprocessing sesuai yang Anda gunakan pada saat training
    cleaned_text = preprocess_text(text)
    prediction = model.predict([cleaned_text])
    return 'Cyberbullying' if prediction[0] == 1 else 'Not Cyberbullying'

# Aplikasi Streamlit
st.title("Cyberbullying Detection App")
st.write("Masukkan tweet untuk memprediksi apakah itu merupakan tweet bullying atau bukan.")

input_text = st.text_area("Input Tweet")
if st.button("Prediksi"):
    result = predict_bullying(input_text)
    st.write(f"Hasil Prediksi: {result}")
