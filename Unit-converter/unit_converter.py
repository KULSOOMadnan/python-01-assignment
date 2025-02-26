# Import required libraries
import streamlit as st
import requests

# API endpoints
UNIT_API_URL = "https://api.unit-converter.io/api/v1/convert"  # Note: This API is not used currently
CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/"

# Configure Streamlit page
st.set_page_config(page_title="Universal Converter", page_icon="🔄", layout="centered")
st.title("🔄 Universal Converter")
st.write("Convert **Units & Currencies** easily! Select a category and get instant results.")

# Define conversion factors dictionary - moved outside function for better performance
CONVERSION_FACTORS = {
    "Length": {
        "meters": 1,
        "feet": 3.28084,
        "inches": 39.3701,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "yards": 1.09361
    },
    "Weight": {
        "kilograms": 1,
        "pounds": 2.20462,
        "ounces": 35.274,
        "grams": 1000
    },
    "Volume": {
        "liters": 1,
        "gallons": 0.264172,
        "milliliters": 1000,
        "cubic_meters": 0.001
    },
    "Time": {
        "seconds": 1,
        "minutes": 1/60,
        "hours": 1/3600,
        "days": 1/86400
    }
}

# Define available categories and their units
CATEGORIES = {
    "Length": ["meters", "feet", "inches", "kilometers", "miles", "yards"],
    "Weight": ["kilograms", "pounds", "ounces", "grams"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liters", "gallons", "milliliters", "cubic_meters"],
    "Time": ["seconds", "minutes", "hours", "days"]
}

# Define supported currencies with their respective countries
CURRENCIES = ["USD", "EUR", "GBP", "INR", "JPY", "PKR", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD",
             "AED", # United Arab Emirates Dirham
             "SGD", # Singapore Dollar
             "HKD", # Hong Kong Dollar
             "MYR", # Malaysian Ringgit
             "THB", # Thai Baht
             "KRW", # South Korean Won
             "SAR", # Saudi Riyal
             "ZAR", # South African Rand
             "BRL", # Brazilian Real
             "MXN", # Mexican Peso
             "RUB", # Russian Ruble
             "TRY", # Turkish Lira
             "IDR", # Indonesian Rupiah
             "NOK", # Norwegian Krone
             "DKK", # Danish Krone
             "PLN", # Polish Złoty
             "ILS", # Israeli Shekel
             "PHP", # Philippine Peso
             "CZK"  # Czech Koruna
            ]

# Dictionary mapping currencies to their country names
CURRENCY_COUNTRIES = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "INR": "Indian Rupee",
    "JPY": "Japanese Yen",
    "PKR": "Pakistani Rupee",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SEK": "Swedish Krona",
    "NZD": "New Zealand Dollar",
    "AED": "United Arab Emirates Dirham",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "MYR": "Malaysian Ringgit",
    "THB": "Thai Baht",
    "KRW": "South Korean Won",
    "SAR": "Saudi Riyal",
    "ZAR": "South African Rand",
    "BRL": "Brazilian Real",
    "MXN": "Mexican Peso",
    "RUB": "Russian Ruble",
    "TRY": "Turkish Lira",
    "IDR": "Indonesian Rupiah",
    "NOK": "Norwegian Krone",
    "DKK": "Danish Krone",
    "PLN": "Polish Złoty",
    "ILS": "Israeli Shekel",
    "PHP": "Philippine Peso",
    "CZK": "Czech Koruna"
}

def convert_temperature(value, from_unit, to_unit):
    """Handle temperature conversions separately due to different conversion formulas"""
    conversions = {
        ("celsius", "fahrenheit"): lambda x: (x * 9/5) + 32,
        ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,
        ("celsius", "kelvin"): lambda x: x + 273.15,
        ("kelvin", "celsius"): lambda x: x - 273.15,
        ("fahrenheit", "kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("kelvin", "fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)

def convert_units(value, from_unit, to_unit, category):
    """Convert units based on category and conversion factors"""
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    try:
        # Convert to base unit first, then to target unit
        base_value = value / CONVERSION_FACTORS[category][from_unit]
        return base_value * CONVERSION_FACTORS[category][to_unit]
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
        return None

def get_conversion_rate(base_currency, target_currency):
    """Fetch currency conversion rates from API"""
    try:
        response = requests.get(f"{CURRENCY_API_URL}{base_currency}")
        if response.status_code == 200:
            return response.json()["rates"].get(target_currency)
        st.error("Failed to fetch conversion rates. Please try again later.")
        return None
    except requests.RequestException as e:
        st.error(f"API request failed: {str(e)}")
        return None

# Create tabs for Unit and Currency Conversion
tabs = st.tabs(["Unit Converter", "Currency Converter"])

# Unit Converter Tab
with tabs[0]:
    st.header("📏 Unit Converter")
    category = st.selectbox("Select Category", list(CATEGORIES.keys()))
    
    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("From", CATEGORIES[category])
    to_unit = col2.selectbox("To", [u for u in CATEGORIES[category] if u != from_unit])
    
    value = st.number_input("Enter Value", value=1.0)
    
    if st.button("Convert", key="unit_convert"):
        result = convert_units(value, from_unit, to_unit, category)
        if result:
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
        else:
            st.error("Conversion failed. Check the units and try again.")

# Currency Converter Tab
with tabs[1]:
    st.header("💰 Currency Converter")
    amount = st.number_input("Enter Amount", min_value=0.01, value=1.0)
    
    # Update currency selection to show country names
    base_currency = st.selectbox("From Currency", 
                               CURRENCIES,
                               format_func=lambda x: f"{x} - {CURRENCY_COUNTRIES[x]}")
    target_currency = st.selectbox("To Currency", 
                                 [c for c in CURRENCIES if c != base_currency],
                                 format_func=lambda x: f"{x} - {CURRENCY_COUNTRIES[x]}")

    if st.button("Convert"):
        conversion_rate = get_conversion_rate(base_currency, target_currency)
        if conversion_rate:
            converted_amount = amount * conversion_rate
            st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

# Footer
st.markdown("""---
✨ **Made with ❤️ using Streamlit**
""")
