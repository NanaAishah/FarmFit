import random
import time
import csv
from datetime import datetime

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
        print("Generated:", sensor_data)
        time.sleep(5)  # simulate every 5 seconds
