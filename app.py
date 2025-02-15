import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("logistic_model.pkl", "rb"))

# Custom CSS for Dark-Themed UI
st.markdown("""
    <style>
        /* Streamlit default dark theme background */
        .stApp {
            background-color: #0e1117;
        }

        /* Main content container */
        .main-container {
            background-color: #1e2130;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.3);
            width: 50%;
            max-width: 600px;
            margin: auto;
            margin-top: 30px;
        }

        /* Title Styling */
        h1 {
            color: #1db954;
            text-align: center;
            font-size: 28px;
        }

        h3 {
            color: #a1a1a1;
            text-align: center;
            font-size: 20px;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #1db954 !important;
            color: white !important;
            font-size: 16px !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            transition: 0.3s;
            border: none;
        }

        /* Hover effect for button */
        .stButton>button:hover {
            background-color: #17a94d !important;
        }

        /* Churn Prediction Result Box */
        .result-box {
            text-align: center;
            padding: 15px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Center the main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# App Title
st.title("📡 Telecom Customer Churn Prediction")
st.write("### Enter customer details below to predict churn ⬇️")

# User Input Form (Ensuring Exact 20 Features Match the Model)
def user_input():
    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
    SeniorCitizen = st.radio("Senior Citizen", [0, 1], horizontal=True)
    Partner = st.radio("Has Partner", ["Yes", "No"], horizontal=True)
    Dependents = st.radio("Has Dependents", ["Yes", "No"], horizontal=True)
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    PhoneService = st.radio("Phone Service", ["Yes", "No"], horizontal=True)
    MultipleLines = st.radio("Multiple Lines", ["Yes", "No", "No phone service"], horizontal=True)
    InternetService = st.radio("Internet Service", ["DSL", "Fiber optic", "No"], horizontal=True)
    OnlineSecurity = st.radio("Online Security", ["Yes", "No", "No internet service"], horizontal=True)
    OnlineBackup = st.radio("Online Backup", ["Yes", "No", "No internet service"], horizontal=True)
    DeviceProtection = st.radio("Device Protection", ["Yes", "No", "No internet service"], horizontal=True)
    TechSupport = st.radio("Tech Support", ["Yes", "No", "No internet service"], horizontal=True)
    StreamingTV = st.radio("Streaming TV", ["Yes", "No", "No internet service"], horizontal=True)
    StreamingMovies = st.radio("Streaming Movies", ["Yes", "No", "No internet service"], horizontal=True)
    Contract = st.radio("Contract", ["Month-to-month", "One year", "Two year"], horizontal=True)
    PaperlessBilling = st.radio("Paperless Billing", ["Yes", "No"], horizontal=True)
    PaymentMethod = st.radio("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], horizontal=True)
    MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0, value=50)
    TotalCharges = tenure * MonthlyCharges  # Derived feature
    AvgMonthlySpend = TotalCharges / tenure if tenure > 0 else 0  # Avoid division by zero

    # Convert categorical values
    gender = 1 if gender == "Male" else 0
    Partner = 1 if Partner == "Yes" else 0
    Dependents = 1 if Dependents == "Yes" else 0
    PhoneService = 1 if PhoneService == "Yes" else 0
    PaperlessBilling = 1 if PaperlessBilling == "Yes" else 0

    # Creating DataFrame to Match Model's 20 Features
    data = {
        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [tenure],
        "PhoneService": [PhoneService],
        "MultipleLines": [1 if MultipleLines == "Yes" else 0],
        "InternetService": [1 if InternetService == "DSL" else 2 if InternetService == "Fiber optic" else 0],
        "OnlineSecurity": [1 if OnlineSecurity == "Yes" else 0],
        "OnlineBackup": [1 if OnlineBackup == "Yes" else 0],
        "DeviceProtection": [1 if DeviceProtection == "Yes" else 0],
        "TechSupport": [1 if TechSupport == "Yes" else 0],
        "StreamingTV": [1 if StreamingTV == "Yes" else 0],
        "StreamingMovies": [1 if StreamingMovies == "Yes" else 0],
        "Contract": [1 if Contract == "One year" else 2 if Contract == "Two year" else 0],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [1 if PaymentMethod == "Electronic check" else 2 if PaymentMethod == "Mailed check" else 3 if PaymentMethod == "Bank transfer (automatic)" else 4],
        "MonthlyCharges": [MonthlyCharges],
        "TotalCharges": [TotalCharges],
        "AvgMonthlySpend": [AvgMonthlySpend],
    }

    return pd.DataFrame(data)

# Get user input
input_df = user_input()

# Predict churn when button is clicked
if st.button("🔍 Predict Churn"):
    prediction = model.predict(input_df)[0]
    
    # Define result styling
    if prediction == 1:
        result_text = "⚠️ Likely to Churn"
        color = "red"
    else:
        result_text = "✅ Not Likely to Churn"
        color = "#1db954"
    
    # Display Result with Styling
    st.markdown(f"""
        <div class="result-box" style="background-color: {color}; color: white;">
            {result_text}
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close styling div
