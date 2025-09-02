
# 🤖 AI-Powered Credit Risk Assessment with Alternative Data

This project demonstrates how artificial intelligence and machine learning can be used to assess credit risk using alternative data sources. It includes a synthetic dataset, model training pipeline, and an interactive Streamlit application.

---

## 📊 Project Overview

Traditional credit scoring models rely heavily on financial history, which excludes millions of individuals without formal records. This project leverages alternative data such as:
- Utility payment behavior
- Social media activity
- Employment history
- Psychometric scores
- Smartphone usage patterns

Using these features, we train a machine learning model to predict credit default risk.

---

## 📁 Dataset

The dataset is synthetically generated and includes the following features:
- `age`
- `income`
- `employment_length`
- `utility_payment_score`
- `social_media_score`
- `psychometric_score`
- `smartphone_usage_score`
- `default` (target variable)

File: `synthetic_credit_data.csv`

---

## 🧠 Model Architecture

We use a Random Forest Classifier to train the model. The pipeline includes:
- Data preprocessing
- Feature scaling
- Model training and evaluation
- Accuracy target: 75%+

---

## 🌐 Streamlit App

The Streamlit app allows users to input feature values and receive a credit risk prediction.

### Usage:
```bash
streamlit run app.py
```

---

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-credit-risk-assessment.git
cd ai-credit-risk-assessment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## 📦 Requirements
- Python 3.7+
- pandas
- scikit-learn
- streamlit
- joblib

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙌 Contributions
Feel free to fork the repository and submit pull requests for improvements.
