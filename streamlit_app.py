import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('model1.pkl')

st.set_page_config(page_title="HR Attrition Predictor", layout="centered")
st.title("🔍 Employee Attrition Prediction")
st.write("Fill in the employee's details to predict if they're likely to leave.")

# Input fields
age = st.slider("Age", 18, 60, 30)
monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
total_working_years = st.slider("Total Working Years", 0, 40, 10)
job_satisfaction = st.selectbox("Job Satisfaction (1-4)", [1, 2, 3, 4])
years_with_manager = st.slider("Years with Current Manager", 0, 20, 5)
job_level = st.selectbox("Job Level (1-5)", [1, 2, 3, 4, 5])
department_rd = st.selectbox("Department: Research & Development?", ["No", "Yes"])
monthly_rate = st.number_input("Monthly Rate", 1000, 25000, 10000)
years_in_current_role = st.slider("Years in Current Role", 0, 15, 4)
employee_number = st.number_input("Employee Number", 1, 10000, 1000)
job_involvement = st.selectbox("Job Involvement (1-4)", [1, 2, 3, 4])
env_satisfaction = st.selectbox("Environment Satisfaction (1-4)", [1, 2, 3, 4])
hourly_rate = st.number_input("Hourly Rate", 10, 150, 60)
marital_status_married = st.selectbox("Is Married?", ["No", "Yes"])

# Convert inputs to model format
input_data = np.array([[
    stock_option_level,
    monthly_income,
    total_working_years,
    job_satisfaction,
    age,
    years_with_manager,
    job_level,
    1 if department_rd == "Yes" else 0,
    monthly_rate,
    years_in_current_role,
    employee_number,
    job_involvement,
    env_satisfaction,
    hourly_rate,
    1 if marital_status_married == "Yes" else 0
]])

# Predict button
if st.button("Predict Attrition"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ The employee is likely to leave.")
    else:
        st.success("✅ The employee is likely to stay.")
