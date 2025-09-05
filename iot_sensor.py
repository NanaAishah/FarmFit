import random
import time
import csv
from datetime import datetime

# Mapping from short names (used in training/model) to full names (for farmers)
FEATURE_NAME_MAP = {
    "N": "Nitrogen (N)",
    "P": "Phosphorus (P)",
    "K": "Potassium (K)",
    "temperature": "Temperature (°C)",
    "humidity": "Humidity (%)",
    "ph": "Soil pH",
    "rainfall": "Rainfall (mm)"
}

def simulate_sensor_data():
    """Simulate IoT sensor data for NPK, temperature, humidity, pH, and rainfall."""
    data = {
        "N": random.randint(0, 140),   # Nitrogen
        "P": random.randint(5, 145),     # Phosphorus
        "K": random.randint(5, 205),     # Potassium
        "temperature": round(random.uniform(8, 45), 2),
        "humidity": round(random.uniform(14, 100), 2),
        "ph": round(random.uniform(3.0, 10.0), 2),
        "rainfall": round(random.uniform(20, 300), 2),  # rainfall in mm
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return data

def get_display_data(sensor_data):
    """Convert internal sensor data (short names) to farmer-friendly display names."""
    display_data = {FEATURE_NAME_MAP.get(k, k): v for k, v in sensor_data.items() if k != "timestamp"}
    display_data["Timestamp"] = sensor_data["timestamp"]
    return display_data

def save_to_csv(data, filename="data/sensor_log.csv"):
    """Save simulated data to CSV for future analysis."""
    fieldnames = ["timestamp", "N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    try:
        with open(filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:  # write header only once
                writer.writeheader()
            writer.writerow(data)
    except FileNotFoundError:
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)

if __name__ == "__main__":
    while True:
        sensor_data = simulate_sensor_data()
        save_to_csv(sensor_data)
        print("Generated:", get_display_data(sensor_data))  # print farmer-friendly version
        time.sleep(5)  # simulate every 5 seconds



