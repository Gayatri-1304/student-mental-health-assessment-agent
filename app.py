import streamlit as st
import joblib
import numpy as np

# ==========================
# Load Model, Scaler and Encoder
# ==========================
model = joblib.load("mental_health_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

st.set_page_config(
    page_title="Student Mental Health Assessment Agent",
    page_icon="🎓"
)

st.title("🎓 Student Mental Health Assessment Agent")
st.write("Enter the student details below to assess mental health.")

# ==========================
# User Inputs
# ==========================

gender = st.selectbox("Gender", [0, 1])

age = st.number_input(
    "Age",
    min_value=15.0,
    max_value=40.0,
    value=21.0
)

course = st.number_input(
    "Course (Encoded)",
    min_value=0,
    value=0
)

year = st.selectbox(
    "Current Year of Study",
    [0, 1, 2, 3]
)

cgpa = st.number_input(
    "CGPA Category (Encoded)",
    min_value=0,
    value=0
)

marital = st.selectbox(
    "Marital Status",
    [0, 1]
)

anxiety = st.selectbox(
    "Do you have Anxiety?",
    [0, 1]
)

panic = st.selectbox(
    "Do you have Panic Attack?",
    [0, 1]
)

specialist = st.selectbox(
    "Visited Mental Health Specialist?",
    [0, 1]
)

# ==========================
# Prediction
# ==========================

if st.button("Predict"):

    input_data = np.array([[
        gender,
        age,
        course,
        year,
        cgpa,
        marital,
        anxiety,
        panic,
        specialist
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    st.subheader("Prediction Result")

    if prediction == "Yes":

        st.error("⚠ Depression Detected")

        st.subheader("Recommendations")

        st.write("✅ Consult a mental health counselor.")
        st.write("✅ Practice meditation or yoga.")
        st.write("✅ Sleep at least 7–8 hours daily.")
        st.write("✅ Maintain a healthy diet.")
        st.write("✅ Talk with trusted friends or family.")
        st.write("✅ Seek professional help if symptoms continue.")

    else:

        st.success("✅ No Depression Detected")

        st.subheader("Recommendations")

        st.write("✅ Continue a healthy lifestyle.")
        st.write("✅ Exercise regularly.")
        st.write("✅ Maintain good sleep habits.")
        st.write("✅ Manage stress effectively.")
        st.write("✅ Stay socially connected.")
