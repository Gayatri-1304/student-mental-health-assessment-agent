# 🎓 Student Mental Health Assessment Agent

## Overview

The Student Mental Health Assessment Agent is an AI-powered application that predicts whether a student is likely to have depression based on survey responses. The system uses a trained Machine Learning model (Logistic Regression) to analyze student information and provide wellness recommendations.

---

## Features

- Predicts depression status using Machine Learning.
- Uses Logistic Regression as the final trained model.
- Provides personalized mental health recommendations.
- User-friendly web interface built with Streamlit.
- Fast and easy to use.

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Machine Learning Model

- Algorithm: Logistic Regression
- Accuracy: 90.48%
- Precision: 100%
- Recall: 71.43%
- F1-Score: 83.33%

---

## Project Structure

```
Student-Mental-Health-Assessment-Agent/
│── app.py
│── requirements.txt
│── README.md
│── mental_health_model.pkl
│── scaler.pkl
│── encoder.pkl
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Student-Mental-Health-Assessment-Agent.git
```

Move to the project folder:

```bash
cd Student-Mental-Health-Assessment-Agent
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Input Features

- Gender
- Age
- Course
- Current Year of Study
- CGPA
- Marital Status
- Anxiety
- Panic Attack
- Visited Mental Health Specialist

---

## Output

The application predicts:

- Depression Detected
- No Depression Detected

It also provides appropriate wellness recommendations based on the prediction.

---

## Author

Developed as an AI and Machine Learning project for Student Mental Health Assessment.
