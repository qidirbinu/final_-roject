{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3495537b-98fb-4e13-8a47-268203529564",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Muat model\n",
    "model = joblib.load('bullying_model.pkl')\n",
    "\n",
    "# Definisikan fungsi untuk prediksi\n",
    "def predict_bullying(text):\n",
    "    # Tambahkan langkah preprocessing sesuai yang Anda gunakan pada saat training\n",
    "    cleaned_text = preprocess_text(text)\n",
    "    prediction = model.predict([cleaned_text])\n",
    "    return 'Cyberbullying' if prediction[0] == 1 else 'Not Cyberbullying'\n",
    "\n",
    "# Aplikasi Streamlit\n",
    "st.title(\"Cyberbullying Detection App\")\n",
    "st.write(\"Masukkan tweet untuk memprediksi apakah itu merupakan tweet bullying atau bukan.\")\n",
    "\n",
    "input_text = st.text_area(\"Input Tweet\")\n",
    "if st.button(\"Prediksi\"):\n",
    "    result = predict_bullying(input_text)\n",
    "    st.write(f\"Hasil Prediksi: {result}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
