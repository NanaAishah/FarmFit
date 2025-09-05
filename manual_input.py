import streamlit as st
import pandas as pd
import joblib
import pickle
import os

# Load trained model
model = joblib.load("best_model.joblib")

# Load label encoder
with open("LE.pkl", "rb") as f:
    label_encoder = pickle.load(f)

def manual_input_form():
    st.subheader("✍️ Manual Input for Crop Recommendation")

    with st.form("manual_input_form"):
        N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
        P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=40)
        K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=60)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)
        ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)

        submitted = st.form_submit_button("🌱 Recommend Crop")

    if submitted:
        input_df = pd.DataFrame([{
            "N": N, "P": P, "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }])

        # Make prediction
        y_pred = model.predict(input_df)[0]
        predicted_crop = label_encoder.inverse_transform([y_pred])[0]

        st.success(f"👉 Recommended Crop: **{predicted_crop}**")

        # Save to history
        log_entry = input_df.copy()
        log_entry["predicted_crop"] = predicted_crop

        os.makedirs("data", exist_ok=True)
        log_file = "data/sensor_log.csv"

        if not os.path.exists(log_file):
            log_entry.to_csv(log_file, index=False)
        else:
            log_entry.to_csv(log_file, mode="a", header=False, index=False)
