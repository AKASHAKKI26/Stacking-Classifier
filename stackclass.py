import streamlit as st
import pickle
import numpy as np
from sklearn.datasets import load_breast_cancer

with open("breast_cancer_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

data = load_breast_cancer()

feature_names = data.feature_names

st.title("Breast Cancer Prediction App")

input_data = []

for feature in features:

    value = st.number_input(
        feature,
        min_value=0.0,
        value=1.0,
        format="%.4f"
    )

    input_data.append(value)

if st.button("Predict"):

    input_array = np.array([input_data])
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("Benign Tumor Detected")
    else:
        st.error("Malignant Tumor Detected")