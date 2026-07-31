import streamlit as st
import pandas as pd
import pickle

# ----------------------------
# Load Trained SVR Model
# ----------------------------
with open("model3.pkl", "rb") as f:
    model = pickle.load(f)

# ----------------------------
# Load Dataset
# ----------------------------
car = pd.read_csv("final.csv")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# ----------------------------
# Title
# ----------------------------
st.title("🚗 Car Price Prediction using Support Vector Regression (SVR)")
st.write("Enter the car details below to predict the estimated selling price.")

# ----------------------------
# User Inputs
# ----------------------------
company = st.selectbox(
    "Company",
    sorted(car["company"].unique())
)

car_model = st.selectbox(
    "Car Model",
    sorted(car[car["company"] == company]["name"].unique())
)

year = st.selectbox(
    "Manufacturing Year",
    sorted(car["year"].unique(), reverse=True)
)

fuel = st.selectbox(
    "Fuel Type",
    sorted(car["fuel_type"].unique())
)

kms = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=10000,
    step=1000
)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "name": [car_model],
        "company": [company],
        "year": [year],
        "kms_driven": [kms],
        "fuel_type": [fuel]
    })

    try:
        prediction = model.predict(input_df)

        # This works for your SVR model output shape (1,1)
        predicted_price = prediction[0][0]

        st.success(f"Estimated Car Price: ₹ {predicted_price:,.2f}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")