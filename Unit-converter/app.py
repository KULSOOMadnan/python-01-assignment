import streamlit as st
import requests


# Function to fetch conversion rates from API
def get_conversion_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"].get(target_currency)
    else:
        st.error("Failed to fetch conversion rates. Please try again later.")
        return None

# Function to fetch historical data
# def get_historical_data(base_currency, target_currency):
#     url = f"https://api.exchangerate-api.com/v4/history/{base_currency}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         rates = data["rates"]
#         dates = list(rates.keys())
#         historical_rates = [rates[date][target_currency] for date in dates]
#         return pd.DataFrame({"Date": dates, "Rate": historical_rates})
#     else:
#         st.error("Failed to fetch historical data. Please try again later.")
#         return None

# Streamlit App
st.title("Unit Converter (Currency)")

# Input fields
amount = st.number_input("Enter Amount", min_value=0.01, value=1.0)
base_currency = st.selectbox("From Currency", ["USD", "EUR", "GBP", "INR", "JPY", "PKR", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"])
target_currency = st.selectbox("To Currency", ["USD", "EUR", "GBP", "INR", "JPY", "PKR", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"])

# Convert button
if st.button("Convert"):
    if base_currency == target_currency:
        st.warning("Please select different currencies for conversion.")
    else:
        conversion_rate = get_conversion_rate(base_currency, target_currency)
        if conversion_rate:
            converted_amount = amount * conversion_rate
            st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            
          