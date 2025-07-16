# 🧠 Employee Attrition Prediction (HR Analytics)

This machine learning app helps HR professionals and analysts predict whether an employee is likely to leave the organization based on multiple job-related and personal factors.

🔗 **Live App**: [Try it on Streamlit](https://employee-attrition-predictionmodel.streamlit.app)

---

## 📊 Features

- Predicts likelihood of employee attrition
- Based on IBM HR Analytics Dataset (from Kaggle)
- Uses a trained **RandomForestClassifier** model
- Built with **Streamlit** for easy interaction
- Supports 15+ features like Age, Income, Job Satisfaction, etc.

---

## 🧪 Dataset

- Source: [IBM HR Analytics Employee Attrition & Performance Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Includes 34 features per employee across roles, performance, income, and satisfaction

---

## 🚀 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas / NumPy
- Joblib (for model serialization)

---

## 🧠 Model Training

- Trained a RandomForestClassifier after comparing it with Logistic Regression, XGBoost, KNN, and VotingClassifier
- Used feature importance to select top 15 predictors
- Achieved **88% test accuracy**

---

## 📦 Installation (for local use)

```bash
git clone https://github.com/your-username/employee-attrition-prediction.git
cd employee-attrition-prediction
pip install -r requirements.txt
streamlit run streamlit_app.py
