import streamlit as st

def convert_units(value, unit_from, unit_to):
    # Dictionary of length units with their values in meters
    length_units = {
        "meter": 1,        # meter
        "centimeter": 0.01,    # centimeter (1 cm = 0.01 meters)
        "millimeter": 0.001,   # millimeter (1 mm = 0.001 meters)
        "kilometer": 1000,    # kilometer (1 km = 1000 meters)
        "mile": 1609.34, # mile (1 mile = 1609.34 meters)
        "yard": 0.9144,  # yard (1 yard = 0.9144 meters)
        "ft": 0.3048,   # foot (1 foot = 0.3048 meters)
    }

    # Check if the units are valid
    if unit_from not in length_units or unit_to not in length_units:
        return "Invalid units. Supported units: meter, centimeter, millimeter, kilometer, mile, yard, ft."
    
    # Convert the value to meters first
    value_in_meters = value * length_units[unit_from]

    # Convert the value in meters to the target unit
    result = value_in_meters / length_units[unit_to]

    return result

# Streamlit UI setup
st.title("Length Unit Converter")  # Set title for the web app

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:", ["meter", "centimeter", "millimeter", "kilometer", "mile", "yard", "ft"]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox(
    "Convert to:", ["meter", "centimeter", "millimeter", "kilometer", "mile", "yard", "ft"]
)

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    st.write(f"Converted Value: {result}")  # Display the result
