import streamlit as st
import joblib
import pandas as pd

# Set the tab title
st.set_page_config(page_title="Machine Failure Prediction")

# Set the page title
st.title("Machine Failure Prediction Project")

# Set header
st.subheader("By Jyotsna Shinde")

# Load the preprocessing pipeline and model
pre = joblib.load("pipeline.joblib")
model = joblib.load("model.joblib")

# Create input boxes
Type = st.selectbox("Machine Type", options=["L", "M", "H"])

Air_temperature = st.number_input(
    "Air Temperature [K]", min_value=250.0, value=300.0
)

Process_temperature = st.number_input(
    "Process Temperature [K]", min_value=250.0, value=310.0
)

Rotational_speed = st.number_input(
    "Rotational Speed [rpm]", min_value=1, value=1500, step=1
)

Torque = st.number_input(
    "Torque [Nm]", min_value=0.0, value=40.0
)

Tool_wear = st.number_input(
    "Tool Wear [min]", min_value=0, value=100, step=1
)

# Prediction button
submit = st.button("Predict Machine Failure")

if submit:

    # Create input dictionary
    data = {
        "Type": [Type],
        "Air temperature [K]": [Air_temperature],
        "Process temperature [K]": [Process_temperature],
        "Rotational speed [rpm]": [Rotational_speed],
        "Torque [Nm]": [Torque],
        "Tool wear [min]": [Tool_wear]
    }

    # Convert dictionary into DataFrame
    xnew = pd.DataFrame(data)

    # Apply preprocessing
    xnew_pre = pre.transform(xnew)

    # Make prediction
    preds = model.predict(xnew_pre)

    # Display result
    if preds[0] == 1:
        st.error("Machine Failure Detected!")
    else:
        st.success("Machine is Operating Normally")
