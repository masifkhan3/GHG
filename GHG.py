import streamlit as st
from PIL import Image

# Function to calculate coal emissions
def calculate_coal_emissions(amount_of_coal):
    emission_factor_coal_co2 = 2200  # kg CO2 per ton of coal
    emission_factor_coal_ch4 = 0.03   # kg CH4 per ton of coal
    emission_factor_coal_n2o = 0.001  # kg N2O per ton of coal

    co2_emissions = amount_of_coal * emission_factor_coal_co2  # in kg
    ch4_emissions = amount_of_coal * emission_factor_coal_ch4  # in kg
    n2o_emissions = amount_of_coal * emission_factor_coal_n2o  # in kg
    return co2_emissions, ch4_emissions, n2o_emissions

# Other emission functions (biomass, gas, diesel) are the same as before

# Function to calculate total GHG emissions in CO2 equivalents
def calculate_total_ghg(co2, ch4, n2o):
    ch4_co2e = ch4 * 25  # Convert CH4 to CO2e
    n2o_co2e = n2o * 298  # Convert N2O to CO2e
    total_ghg = (co2 + ch4_co2e + n2o_co2e) / 1000  # Convert kg to mton
    return total_ghg

# Function to compare GHG emissions with NEQ
def compare_with_ne_quotient(total_ghg, neq):
    if total_ghg > neq:
        return "Total GHG emissions exceed the NEQ."
    elif total_ghg < neq:
        return "Total GHG emissions are below the NEQ."
    else:
        return "Total GHG emissions are equal to the NEQ."

# Main Streamlit app
def main():
    st.title("Enhanced Greenhouse Gas Emission Dashboard")
    st.write("Developed by [Your Name Here]")

    # Sidebar for GHG calculations
    st.sidebar.title("Emission Calculator")
    amount_of_coal = st.sidebar.number_input("Enter coal burned (tons):", min_value=0.0, value=0.0)
    amount_of_biomass = st.sidebar.number_input("Enter biomass burned (tons):", min_value=0.0, value=0.0)
    amount_of_gas = st.sidebar.number_input("Enter natural gas burned (MMBtu):", min_value=0.0, value=0.0)
    amount_of_diesel = st.sidebar.number_input("Enter diesel burned (liters):", min_value=0.0, value=0.0)
    neq = st.sidebar.number_input("Enter National Emission Quotient (NEQ):", min_value=0.0, value=0.0)
    
    # Calculation
    coal_emissions = calculate_coal_emissions(amount_of_coal)
    biomass_emissions = calculate_biomass_emissions(amount_of_biomass)
    gas_emissions = calculate_gas_emissions(amount_of_gas)
    diesel_emissions = calculate_diesel_emissions(amount_of_diesel)

    total_ghg = (
        coal_emissions[0] + biomass_emissions[0] + gas_emissions[0] + diesel_emissions[0],
        coal_emissions[1] + biomass_emissions[1] + gas_emissions[1] + diesel_emissions[1],
        coal_emissions[2] + biomass_emissions[2] + gas_emissions[2] + diesel_emissions[2]
    )

    total_ghg_value = calculate_total_ghg(total_ghg[0], total_ghg[1], total_ghg[2])
    st.sidebar.write(f"Total GHG emissions: {total_ghg_value:.2f} mton CO2e")
    comparison_result = compare_with_ne_quotient(total_ghg_value, neq)
    st.sidebar.write(comparison_result)

    # Interactive Gas Dashboard
    st.header("Gas Dashboard")

    gases = ["CO (Carbon Monoxide)", "H2 (Hydrogen)", "CH4 (Methane)", "CO2 (Carbon Dioxide)"]
    selected_gas = st.selectbox("Select a gas to view details:", gases)

    if selected_gas == "CO (Carbon Monoxide)":
        st.subheader("CO (Carbon Monoxide)")
        st.write("Carbon monoxide (CO) is a colorless, odorless gas produced from the incomplete combustion of carbon-containing fuels.")
        co_image = Image.open("path_to_co_image.jpg")  # Replace with your image path
        st.image(co_image, caption="CO Molecule", use_column_width=True)

    elif selected_gas == "H2 (Hydrogen)":
        st.subheader("H2 (Hydrogen)")
        st.write("Hydrogen (H2) is the lightest element and a clean fuel, emitting only water when burned.")
        h2_image = Image.open("path_to_hydrogen_image.jpg")  # Replace with your image path
        st.image(h2_image, caption="H2 Molecule", use_column_width=True)

    elif selected_gas == "CH4 (Methane)":
        st.subheader("CH4 (Methane)")
        st.write("Methane (CH4) is a potent greenhouse gas emitted during the production and transport of coal, oil, and natural gas.")
        ch4_image = Image.open("path_to_ch4_image.jpg")  # Replace with your image path
        st.image(ch4_image, caption="CH4 Molecule", use_column_width=True)

    elif selected_gas == "CO2 (Carbon Dioxide)":
        st.subheader("CO2 (Carbon Dioxide)")
        st.write("Carbon dioxide (CO2) is a greenhouse gas resulting primarily from burning fossil fuels and deforestation.")
        co2_image = Image.open("path_to_co2_image.jpg")  # Replace with your image path
        st.image(co2_image, caption="CO2 Molecule", use_column_width=True)

    st.write("Use the sidebar to calculate greenhouse gas emissions from various fuel sources and compare them with the NEQ.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
