import streamlit as st
import pandas as pd
import joblib
import pickle
import os
from iot_sensor import simulate_sensor_data

# Load trained model
model = joblib.load("best_model.joblib")

# Load label encoder
with open("LE.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# App Title
st.set_page_config(page_title="Farm Fit", page_icon="🌱", layout="wide")
st.title("🌱 FARM FIT")
st.markdown("Smart crop recommendation powered by **IoT sensors + Machine Learning** 🚜🌾")

# --- IoT Sensor Simulation Section ---
st.subheader("📡 IoT Sensor Simulation")

if st.button("🔄 Generate Sensor Data"):
    # Simulate data
    sensor_data = simulate_sensor_data()
    
    # Show nicely
    st.success("✅ Sensor data generated successfully!")
    st.json(sensor_data)

    # Convert to DataFrame for prediction
    input_df = pd.DataFrame([{
        "N": sensor_data["N"],
        "P": sensor_data["P"],
        "K": sensor_data["K"],
        "temperature": sensor_data["temperature"],
        "humidity": sensor_data["humidity"],
        "ph": sensor_data["ph"],
        "rainfall": sensor_data["rainfall"]
    }])

    # Make prediction
    y_pred = model.predict(input_df)[0]
    predicted_crop = label_encoder.inverse_transform([y_pred])[0]

    # Display result in a styled box (without confidence score)
    st.markdown("### 🌾 Recommended Crop")
    st.success(f"👉 **{predicted_crop}**")

    # --- Save sensor data + prediction to CSV ---
    log_entry = input_df.copy()
    log_entry["predicted_crop"] = predicted_crop

    os.makedirs("data", exist_ok=True)  # ensure folder exists
    log_file = "data/sensor_log.csv"

    if not os.path.exists(log_file):
        log_entry.to_csv(log_file, index=False)
    else:
        log_entry.to_csv(log_file, mode="a", header=False, index=False)

else:
    st.info("Click the button above to generate IoT sensor data and see recommendations.")

# --- History Section ---
st.markdown("---")
st.subheader("📊 Historical IoT Data")

try:
    history = pd.read_csv("data/sensor_log.csv")
    st.dataframe(history.tail(10))
except FileNotFoundError:
    st.info("No historical IoT data yet. Start by generating some sensor data.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Copyright © 2025")




