# Electricity Bill Prediction

A beginner-friendly machine learning project that predicts the estimated monthly electricity bill based on household appliance usage, city, electricity company, and month.


## About the Project

This project uses **Linear Regression** to estimate the monthly electricity bill of a household based on different household and appliance-related features.

The trained machine learning model is integrated into a simple **Streamlit web application** where users can enter their details and get an estimated electricity bill.

## Features

* Select City
* Select Electricity Company
* Enter appliance usage
* Select Month
* Get estimated monthly electricity bill
* Choose between exact estimate and approximate range
* Simple and easy-to-use interface

## Machine Learning

**Algorithm:** Linear Regression

**Categorical Encoding:** One-Hot Encoding

The model uses the following features:

* City
* Electricity Company
* Fan Usage
* Refrigerator Usage
* Air Conditioner Usage
* Television Usage
* Monitor Usage
* Month

## Model Performance

| Metric   |   Score |
| -------- | ------: |
| MAE      | ₹596.27 |
| RMSE     | ₹693.65 |
| R² Score |   0.578 |

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit

## Project Structure

```text
electricity-bill-prediction/
│
├── model/
│   └── electricity_bill_model.pkl
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

Dataset:

The project uses the **Indian Household Electricity Consumption Dataset** from Kaggle.

**[Dataset on Kaggle](https://www.kaggle.com/datasets/suraj520/indian-household-electricity-bill)**

