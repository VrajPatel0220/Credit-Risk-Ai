import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model/credit_model.pkl')

st.title("AI-Powered Credit Risk Assessment")

# Input form
age = st.slider("Age", 18, 70, 30)
income = st.number_input("Monthly Income", min_value=10000, max_value=200000, value=50000)
employment_length = st.slider("Employment Length (years)", 0, 40, 5)
utility_score = st.slider("Utility Payment Score", 0.0, 1.0, 0.5)
social_score = st.slider("Social Media Score", 0.0, 1.0, 0.5)
psychometric_score = st.slider("Psychometric Score", 0.0, 1.0, 0.5)
smartphone_score = st.slider("Smartphone Usage Score", 0.0, 1.0, 0.5)

# Predict
if st.button("Assess Credit Risk"):
    input_data = pd.DataFrame([[age, income, employment_length, utility_score,
                                social_score, psychometric_score, smartphone_score]],
                              columns=['age', 'income', 'employment_length',
                                       'utility_payment_score', 'social_media_score',
                                       'psychometric_score', 'smartphone_usage_score'])
    prediction = model.predict(input_data)[0]
    st.success("Prediction: {}".format("High Risk" if prediction == 1 else "Low Risk"))
