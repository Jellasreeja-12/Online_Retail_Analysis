import joblib
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(__file__)

# Build full path to the model file
model_path = os.path.join(BASE_DIR, "churn_model.pkl")

# Load the model

model = joblib.load(model_path)

# Title and description
st.title("Customer Churn Prediction")
st.write("Enter customer RFM values to predict whether they are likely to churn.")

# Input boxes
recency = st.number_input(
    "Recency (days since last purchase)", min_value=0, value=30)
frequency = st.number_input(
    "Frequency (number of orders)", min_value=0, value=5)
monetary = st.number_input(
    "Monetary (total amount spent in £)", min_value=0, value=500)

# Predict button
# Predict button
if st.button("Predict"):

    input_data = pd.DataFrame([[recency, frequency, monetary]],
                              columns=["Recency", "Frequency", "Monetary"])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.write("Prediction:", prediction)
    st.write("Probability:", probability)

    if prediction == 1:
        st.error(
            f"🔴 High Churn Risk — {round(probability * 100, 1)}% probability of churning")
    else:
        st.success(
            f"🟢 Low Churn Risk — {round(probability * 100, 1)}% probability of churning")
