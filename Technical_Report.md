# 🌱 FarmFit – Smart Crop Recommendation System  

FarmFit is an AI-powered crop recommendation system that leverages **IoT sensor data** and **Machine Learning** to assist farmers in making smarter agricultural decisions.  

---

## Project Overview  
Modern agriculture faces challenges such as declining soil fertility, climate variability, and inefficient resource use. FarmFit addresses this by:  
- Collecting soil and environmental data (N, P, K levels, temperature, humidity, rainfall, etc.)  
- Applying supervised machine learning models  
- Recommending the most suitable crop for cultivation  

---

##  Methodology  

### **1. Data Collection**  
- Dataset used: [Kaggle Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)  
- Features include:  
  - **Soil nutrients**: Nitrogen (N), Phosphorus (P), Potassium (K)  
  - **Environmental factors**: Temperature, Humidity, pH, Rainfall  

### **2. Data Preprocessing**  
- Data has no missing values  
- Standardized/normalized numerical features  
- Split dataset into **training** (80%) and **testing** (20%)  

### **3. Model Training & Evaluation**  
We experimented with multiple machine learning models:  
- **Logistic Regression**  
- **Random Forest Classifier**  
- **Decision Tree**  
- **Support Vector Machine (SVM)**  
- **XGBoost**  

**Best Performing Model**:  
- **Random Forest Classifier** with **accuracy ~99%** on test data  
- Chosen as the final deployment model  

---

## Deployment  

### **1. Streamlit App**  
- Built an interactive UI using streamlit 
- IoT simulation module generates live sensor-like data  

### **2. Hosting**  
- Deployed on **Streamlit Cloud**  
- Requirements managed via `requirements.txt`  
- Model serialized using `joblib`
- https://farmfit-crop-recommendation.streamlit.app/

---

## Results & Insights  
- Machine learning can accurately recommend crops using basic soil/environment data  
- Demonstrates potential of **AI + IoT** in agriculture  
- Helps improve yield and resource management  

---

## Future Improvements  
- Integration with **real IoT devices** (soil sensors, weather stations)  
- Adding **fertilizer recommendation**  
- Scaling to handle **region-specific datasets**  
- Deploying as a **mobile app** for offline usage  

---

## 🙌 Contributors  
- Abubakar Nana Aishah (@NanaAishah)
- Rosheedat Dasola Busari (@RosheedatDasola)
- Abubakar Khadeejah (@newsuccesskdj) 

