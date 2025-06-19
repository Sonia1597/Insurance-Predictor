
import streamlit as st
import numpy as np
import pandas as pd
import joblib  # or use pickle if you saved with pickle

# Load trained Random Forest model
model = joblib.load("random_forest_model.pkl")

# Streamlit UI
st.title("Insurance Cost Prediction using Random Forest Regressor")
st.write("Provide the user details below to predict insurance charges.")

# Input fields
age = st.slider("Age", 18, 65, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Encode the inputs like training data
data = {
    'age': age,
    'bmi': bmi,
    'children': children,
    'sex_male': 1 if sex == 'male' else 0,
    'smoker_yes': 1 if smoker == 'yes' else 0,
    'region_northwest': 1 if region == 'northwest' else 0,
    'region_southeast': 1 if region == 'southeast' else 0,
    'region_southwest': 1 if region == 'southwest' else 0
    # region_northeast is captured when all 3 other region dummies are 0
}

input_df = pd.DataFrame([data])

# Prediction
if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Insurance Charges: ₹{prediction:.2f}")
