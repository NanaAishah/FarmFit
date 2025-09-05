import streamlit as st
import pandas as pd
import joblib
import pickle
import os
from iot_sensor import simulate_sensor_data, get_display_data
from manual_input import manual_input_form  # make sure manual_input.py exists

# ------------------------------
# Load Model and Label Encoder
# ------------------------------
model = joblib.load("best_model.joblib")

with open("LE.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# ------------------------------
# App Config
# ------------------------------
st.set_page_config(page_title="Farm Fit", page_icon="🌱", layout="wide")
st.title("🌱 FARM FIT")
st.markdown("**Smart Crop Recommendation System**")

# ------------------------------
# Sidebar Navigation
# ------------------------------
page = st.sidebar.radio("📌 Navigate", ["📡 IoT Sensor Simulation", "✍️ Manual Input", "📊 History"])

# ------------------------------
# Page 1: IoT Sensor Simulation
# ------------------------------
if page == "📡 IoT Sensor Simulation":
    st.subheader("📡 IoT Sensor Simulation")

    if st.button("🔄 Generate Sensor Data"):
        # Simulate IoT data
        sensor_data = simulate_sensor_data()

        # Show farmer-friendly version
        st.success("✅ Sensor data generated successfully!")
        st.json(get_display_data(sensor_data))

        # Prepare input with short names for ML model
        input_df = pd.DataFrame([{
            "N": sensor_data["N"],
            "P": sensor_data["P"],
            "K": sensor_data["K"],
            "temperature": sensor_data["temperature"],
            "humidity": sensor_data["humidity"],
            "ph": sensor_data["ph"],
            "rainfall": sensor_data["rainfall"]
        }])

        # Predict crop
        y_pred = model.predict(input_df)[0]
        predicted_crop = label_encoder.inverse_transform([y_pred])[0]

        # Display result
        st.markdown("### 🌾 Recommended Crop")
        st.success(f"👉 **{predicted_crop}**")

        # Save sensor data + prediction
        log_entry = input_df.copy()
        log_entry["predicted_crop"] = predicted_crop

        os.makedirs("data", exist_ok=True)
        log_file = "data/sensor_log.csv"

        if not os.path.exists(log_file):
            log_entry.to_csv(log_file, index=False)
        else:
            log_entry.to_csv(log_file, mode="a", header=False, index=False)

    else:
        st.info("Click the button above to generate IoT sensor data and see recommendations.")

# ------------------------------
# Page 2: Manual Input
# ------------------------------
elif page == "✍️ Manual Input":
    manual_input_form()

# ------------------------------
# Page 3: History
# ------------------------------
elif page == "📊 History":
    st.subheader("📊 Historical IoT & Manual Input Data")
    try:
        history = pd.read_csv("data/sensor_log.csv")
        st.dataframe(history.tail(20))
    except FileNotFoundError:
        st.info("No historical data yet. Start by generating or entering data.")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025")






