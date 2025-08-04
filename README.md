# ⚡ Power System Fault Detection Using Machine Learning

This project presents a machine learning-based solution to automatically detect and classify faults in power distribution systems. By analyzing electrical parameters such as voltage, current, and phasor measurements, the model predicts fault types, helping maintain the stability and efficiency of the power grid.

---

## 📌 Problem Statement

Power distribution systems are prone to various types of faults such as line-to-ground, line-to-line, and three-phase faults. These faults can disrupt power supply and reduce system reliability. The challenge lies in accurately detecting and classifying these faults using electrical data, ensuring quick recovery and grid stability.

---

## 🚀 Proposed Solution

- Use supervised machine learning (Random Forest or SVM) to classify fault types.
- Train the model using labeled electrical parameter data.
- Deploy the model to IBM Watson Studio with an accessible API endpoint.
- Enable real-time predictions to support automated fault detection.

---

## 🛠️ Tools and Technologies

- **IBM Watson Studio** (Model development and deployment)
- **IBM Cloud Object Storage** (Data storage)
- **IBM Machine Learning Runtime**
- **Python**
- **Random Forest Classifier / SVM**
- **Supervised Learning Approach**

---

## 📊 Dataset

- Source: Kaggle (public dataset)
- Features used: voltage, current, phasor measurements
- Preprocessing included normalization and cleaning

---

## 🧠 Algorithm & Deployment

- **Algorithm:** Random Forest Classifier (chosen for performance)
- **Input:** Voltage, current, and phasor readings
- **Training:** Labeled fault data using supervised learning
- **Deployment:** IBM Watson Studio with real-time API endpoint for scoring

---

## 🔗 API Endpoint

The trained model has been deployed to IBM Cloud and is accessible via the following public endpoint:
https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/844683d5-2809-4351-84fb-1fb51ebd430c/predictions?version=2021-05-01

Use the script `predict_api.py` to test the API with your own input data.

---

## 🐍 Sample Prediction Code (Python)

```python
import requests

# Replace with your actual Bearer token
mltoken = "your_IBM_cloud_token"

payload_scoring = {
    "input_data": [
        {
            "fields": ["voltage", "current", "phasor"],
            "values": [[230.0, 5.2, 0.98]]
        }
    ]
}

url = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/844683d5-2809-4351-84fb-1fb51ebd430c/predictions?version=2021-05-01"

response = requests.post(
    url,
    json=payload_scoring,
    headers={"Authorization": "Bearer " + mltoken}
)

print("Scoring response:")
print(response.json())



