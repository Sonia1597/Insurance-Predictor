# 🏥 Insurance Cost Predictor

A machine learning web app that predicts **insurance charges** based on user input, using a trained **Random Forest Regressor** model.

🔗 **Live App**: [insurance-predictor-sonia.streamlit.app](https://insurance-predictor-sonia.streamlit.app/)

---

## 📌 Features

- Predicts insurance costs using:
  - Age
  - Gender
  - BMI
  - Number of children
  - Smoking status
  - Region of residence
- Interactive and user-friendly interface built with **Streamlit**
- Model deployed online and ready for real-time predictions

---

## 🚀 Demo

![App Screenshot](https://raw.githubusercontent.com/Sonia1597/Insurance-Predictor/main/assets/demo.png)  
> _Note: Add `assets/demo.png` screenshot manually if needed._

---

## 🧠 Machine Learning Model

- Algorithm: **Random Forest Regressor**
- Trained on the **Medical Cost Personal Dataset** (Kaggle)
- Hyperparameters tuned:
  - `n_estimators = 150`
  - `max_depth = 10`
  - `min_samples_split = 2`
  - `min_samples_leaf = 2`
  - `max_features = 'log2'`

---

## 📂 Project Structure

Insurance-Predictor/
│
├── app.py # Streamlit web app
├── random_forest_model.pkl # Saved machine learning model
├── requirements.txt # Project dependencies
├── README.md # This file
└── assets/
└── ![image](https://github.com/user-attachments/assets/0edf3cd9-6342-43a5-988a-918ccf3ed14d)





