# 🔌 Power System Fault Detection Using Machine Learning

This project focuses on detecting and classifying faults in power distribution systems using machine learning techniques. The model is trained on electrical parameters such as voltage, current, and phasor measurements to identify different fault types and enhance grid stability.

---

## 📌 Problem Statement

Power distribution networks are prone to faults like line-to-ground, line-to-line, and three-phase faults. These can disrupt the power supply and affect system reliability. This project aims to develop a machine learning-based solution that accurately detects and classifies such faults to improve response time and grid performance.

---

## 🚀 Proposed Solution

- A supervised learning model is trained on fault data to classify fault types.
- Random Forest (or SVM based on performance) is used as the classifier.
- Real-time fault predictions are enabled using IBM Watson Studio deployment.
- The model supports faster recovery actions and improves overall system efficiency.

---

## 🛠️ Tools and Technologies

- **IBM Watson Studio** (Model development & deployment)
- **IBM Cloud Object Storage** (Dataset storage)
- **Python**
- **Random Forest Classifier / SVM**
- **Supervised Learning**

---

## 🧪 Dataset

- Sourced from Kaggle (public dataset)
- Includes: voltage, current, and phasor readings
- Preprocessing steps: normalization, missing value handling

---

## 📊 Model Training and Deployment

- Trained using labeled data for fault classification
- Deployed on IBM Watson Studio with an API endpoint for real-time predictions
- Example Python integration for predictions:
  
```python
response_scoring = requests.post('<API_ENDPOINT>',
    json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
