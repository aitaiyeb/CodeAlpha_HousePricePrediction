import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction App")
st.write("Predict the estimated price of a house based on its features using Machine Learning!")

# Currency selection options with symbols and conversion rates
currencies = {
    "USD ($)": {"symbol": "$", "rate": 1.0},
    "BDT (৳)": {"symbol": "৳", "rate": 118.0},
    "INR (₹)": {"symbol": "₹", "rate": 83.0},
    "EUR (€)": {"symbol": "€", "rate": 0.92}
}

selected_currency = st.selectbox("Select Currency", options=list(currencies.keys()))
curr_info = currencies[selected_currency]

# Training a simple model
X_train = np.array([
    [1000, 2, 5],
    [1500, 3, 10],
    [2000, 4, 2],
    [2500, 4, 1],
    [800, 1, 15],
    [1200, 2, 8],
    [1800, 3, 4]
])
y_train = np.array([150000, 220000, 320000, 400000, 100000, 180000, 280000])

model = LinearRegression()
model.fit(X_train, y_train)

st.subheader("Enter Property Details:")
area = st.number_input("Area (in Square Feet)", min_value=500, max_value=10000, value=1500, step=50)
bedrooms = st.slider("Number of Bedrooms", min_value=1, max_value=10, value=3)
age = st.slider("Age of House (in years)", min_value=0, max_value=50, value=5)

if st.button("Predict Price", type="primary"):
    user_input = np.array([[area, bedrooms, age]])
    base_price = model.predict(user_input)[0]
    converted_price = base_price * curr_info["rate"]
    
    st.subheader("Estimated House Price:")
    st.success(f"{curr_info['symbol']}{converted_price:,.2f}")