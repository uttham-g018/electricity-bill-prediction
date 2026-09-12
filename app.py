import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("model/electricity_bill_model.pkl")


# Page settings
st.set_page_config(
    page_title="Electricity Bill Prediction",
    page_icon="⚡"
)


# Title
st.title(" Electricity Bill Prediction")

st.write(
    "Enter the household details below to estimate the monthly electricity bill."
)

st.divider()


# City and Company
col1, col2 = st.columns(2)

with col1:
    city = st.selectbox(
        "City",
        [
            "Hyderabad",
            "Vadodara",
            "Shimla",
            "Mumbai",
            "Ratnagiri",
            "New Delhi",
            "Dahej",
            "Ahmedabad",
            "Noida",
            "Nagpur",
            "Chennai",
            "Faridabad",
            "Kolkata",
            "Pune",
            "Gurgaon",
            "Navi Mumbai"
        ]
    )

with col2:
    company = st.selectbox(
        "Electricity Company",
        [
            "Tata Power Company Ltd.",
            "NHPC",
            "Jyoti Structure",
            "Power Grid Corp",
            "Ratnagiri Gas and Power Pvt. Ltd. (RGPPL)",
            "Adani Power Ltd.",
            "Kalpataru Power",
            "Orient Green",
            "Sterlite Power Transmission Ltd",
            "Neueon Towers / Sujana Towers Ltd.",
            "KEC International",
            "Indowind Energy",
            "Unitech Power Transmission Ltd.",
            "Bonfiglioli Transmission Pvt. Ltd.",
            "SJVN Ltd.",
            "Maha Transco – Maharashtra State Electricity Transmission Co, Ltd.",
            "L&T Transmission & Distribution",
            "Guj Ind Power",
            "Torrent Power Ltd.",
            "Reliance Energy",
            "GE T&D India Limited",
            "NTPC Pvt. Ltd.",
            "Optibelt Power Transmission India Private Limited",
            "CESC",
            "Ringfeder Power Transmission India Pvt. Ltd.",
            "Reliance Power",
            "JSW Energy Ltd.",
            "Sunil Hitech Eng",
            "Toshiba Transmission & Distribution Systems (India) Pvt. Ltd.",
            "Jaiprakash Power",
            "TransRail Lighting",
            "NLC India"
        ]
    )


# Appliance usage
st.subheader("Appliance Usage")

col1, col2 = st.columns(2)

with col1:

    fan = st.number_input(
        "Fan Usage (hours/day)",
        min_value=5,
        max_value=23,
        value=10
    )

    refrigerator = st.number_input(
        "Refrigerator Usage (hours/day)",
        min_value=17,
        max_value=23,
        value=20
    )

    air_conditioner = st.number_input(
        "Air Conditioner Usage (hours/day)",
        min_value=0,
        max_value=3,
        value=2
    )

with col2:

    television = st.number_input(
        "Television Usage (hours/day)",
        min_value=3,
        max_value=22,
        value=8
    )

    monitor = st.number_input(
        "Monitor Usage (hours/day)",
        min_value=1,
        max_value=12,
        value=2
    )

    month = st.selectbox(
        "Month",
        range(1, 13),
        format_func=lambda x: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ][x - 1]
    )


st.divider()


# Prediction type
st.subheader("Prediction")

prediction_type = st.radio(
    "Choose prediction type:",
    ["Exact Estimate", "Estimated Range"],
    horizontal=True
)


# Buttons
col1, col2 = st.columns(2)

with col1:
    predict = st.button(
        " Predict Electricity Bill",
        type="primary",
        use_container_width=True
    )

with col2:
    reset = st.button(
        " Reset",
        use_container_width=True
    )


# Reset
if reset:
    st.rerun()


# Prediction
if predict:

    input_data = pd.DataFrame({
        "City": [city],
        "Company": [company],
        "Fan": [fan],
        "Refrigerator": [refrigerator],
        "AirConditioner": [air_conditioner],
        "Television": [television],
        "Monitor": [monitor],
        "Month": [month]
    })

    prediction = model.predict(input_data)[0]

    st.divider()

    st.success("Prediction completed!")

    if prediction_type == "Exact Estimate":

        st.metric(
            "Estimated Monthly Electricity Bill",
            f"₹{prediction:,.2f}"
        )

    else:

        lower = prediction * 0.90
        upper = prediction * 1.10

        st.metric(
            "Estimated Monthly Electricity Bill",
            f"₹{prediction:,.2f}"
        )

        st.info(
            f"Approximate expected range: ₹{lower:,.2f} – ₹{upper:,.2f}"
        )

        st.caption(
            "The range is an approximate ±10% range around the model prediction, "
            "not a statistically calculated prediction interval."
        )


# Model performance
st.divider()

st.subheader("Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("MAE", "₹596.27")

with col2:
    st.metric("RMSE", "₹693.65")

with col3:
    st.metric("R² Score", "0.578")

