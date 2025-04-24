import streamlit as st
import pandas as pd
import pickle
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the trained Prophet model
try:
    with open('prophet_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: prophet_model.pkl not found. Please ensure the model file is present.")
    st.stop()


st.title("Tesla Stock Price Prediction")

# Input for prediction period
periods_input = st.number_input("Enter the number of periods to forecast (months):", min_value=1, value=24)


if st.button("Predict"):
    # Create future dataframe
    future = model.make_future_dataframe(periods=periods_input, freq='M')

    # Make prediction
    forecast = model.predict(future)

    # Display the forecast
    st.subheader("Forecast Data")
    st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods_input))


    # Plot the forecast
    st.subheader("Forecast Plot")
    fig = model.plot(forecast)
    plt.title("Prévision du prix de l'action Tesla (Prophet)")
    plt.xlabel("Date")
    plt.ylabel("Prix de clôture (USD)")
    plt.grid()
    st.pyplot(fig)


    # Display components
    st.subheader("Forecast Components")
    fig2 = model.plot_components(forecast)
    st.pyplot(fig2)