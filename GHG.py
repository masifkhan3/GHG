import streamlit as st
import matplotlib.pyplot as plt

# Function to calculate coal emissions
def calculate_coal_emissions(amount_of_coal):
    emission_factor_coal_co2 = 2200  # kg CO2 per ton of coal
    emission_factor_coal_ch4 = 0.03   # kg CH4 per ton of coal
    emission_factor_coal_n2o = 0.001  # kg N2O per ton of coal

    co2_emissions = amount_of_coal * emission_factor_coal_co2  # in kg
    ch4_emissions = amount_of_coal * emission_factor_coal_ch4  # in kg
    n2o_emissions = amount_of_coal * emission_factor_coal_n2o  # in kg
    return co2_emissions, ch4_emissions, n2o_emissions

# (The rest of the emission calculation functions remain the same)

# Function to calculate total GHG emissions in CO2 equivalents
def calculate_total_ghg(co2, ch4, n2o):
    ch4_co2e = ch4 * 25  # Convert CH4 to CO2e
    n2o_co2e = n2o * 298  # Convert N2O to CO2e
    total_ghg = (co2 + ch4_co2e + n2o_co2e) / 1000  # Convert kg to mton
    return total_ghg

# Function to compare total GHG emissions with National Emission Quotient (NEQ)
def compare_with_ne_quotient(total_ghg, neq):
    if total_ghg > neq:
        return "Total GHG emissions exceed the NEQ."
    elif total_ghg < neq:
        return "Total GHG emissions are below the NEQ."
    else:
        return "Total GHG emissions are equal to the NEQ."

# Function to generate a pie chart for GHG emissions breakdown
def plot_emissions_breakdown(data, labels):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title("🌍 Greenhouse Gas Emission Calculator")
    st.write("Calculate and compare emissions from coal, biomass, natural gas, and diesel oil combustion.")

    # Section: Coal
    with st.container():
        st.markdown("<h3 style='color: #FF9999;'>Coal Emissions</h3>", unsafe_allow_html=True)
        amount_of_coal = st.number_input("Enter the amount of coal burned (tons):", min_value=0.0, value=0.0)
        coal_emissions = calculate_coal_emissions(amount_of_coal)
        st.write(f"CO2 emissions from coal: {coal_emissions[0]/1000:.2f} mton CO2")
        st.write(f"CH4 emissions from coal: {coal_emissions[1]/1000:.4f} mton CH4")
        st.write(f"N2O emissions from coal: {coal_emissions[2]/1000:.4f} mton N2O")

    # Section: Biomass
    with st.container():
        st.markdown("<h3 style='color: #66B2FF;'>Biomass Emissions</h3>", unsafe_allow_html=True)
        amount_of_biomass = st.number_input("Enter the amount of biomass burned (tons):", min_value=0.0, value=0.0)
        biomass_emissions = calculate_biomass_emissions(amount_of_biomass)
        st.write(f"CO2 emissions from biomass: {biomass_emissions[0]/1000:.2f} mton CO2")
        st.write(f"CH4 emissions from biomass: {biomass_emissions[1]/1000:.4f} mton CH4")
        st.write(f"N2O emissions from biomass: {biomass_emissions[2]/1000:.4f} mton N2O")

    # Section: Natural Gas
    with st.container():
        st.markdown("<h3 style='color: #99FF99;'>Natural Gas Emissions</h3>", unsafe_allow_html=True)
        amount_of_gas = st.number_input("Enter the amount of natural gas burned (MMBtu):", min_value=0.0, value=0.0)
        gas_emissions = calculate_gas_emissions(amount_of_gas)
        st.write(f"CO2 emissions from gas: {gas_emissions[0]/1000:.2f} mton CO2")
        st.write(f"CH4 emissions from gas: {gas_emissions[1]/1000:.4f} mton CH4")
        st.write(f"N2O emissions from gas: {gas_emissions[2]/1000:.4f} mton N2O")

    # Section: Diesel
    with st.container():
        st.markdown("<h3 style='color: #FFCC99;'>Diesel Emissions</h3>", unsafe_allow_html=True)
        amount_of_diesel = st.number_input("Enter the amount of diesel oil burned (liters):", min_value=0.0, value=0.0)
        diesel_emissions = calculate_diesel_emissions(amount_of_diesel)
        st.write(f"CO2 emissions from diesel: {diesel_emissions[0]/1000:.2f} mton CO2")
        st.write(f"CH4 emissions from diesel: {diesel_emissions[1]/1000:.4f} mton CH4")
        st.write(f"N2O emissions from diesel: {diesel_emissions[2]/1000:.4f} mton N2O")

    # Calculate total GHG emissions
    total_ghg = (
        coal_emissions[0] + biomass_emissions[0] + gas_emissions[0] + diesel_emissions[0],
        coal_emissions[1] + biomass_emissions[1] + gas_emissions[1] + diesel_emissions[1],
        coal_emissions[2] + biomass_emissions[2] + gas_emissions[2] + diesel_emissions[2]
    )

    total_ghg_value = calculate_total_ghg(total_ghg[0], total_ghg[1], total_ghg[2])
    st.write(f"**Total GHG emissions (in mton CO2e):** {total_ghg_value:.2f} mton CO2e")

    # Emission Breakdown Chart
    st.markdown("<h3 style='color: #4CAF50;'>Emissions Breakdown</h3>", unsafe_allow_html=True)
    emissions_data = [coal_emissions[0], biomass_emissions[0], gas_emissions[0], diesel_emissions[0]]
    fuel_labels = ['Coal', 'Biomass', 'Natural Gas', 'Diesel']
    plot_emissions_breakdown(emissions_data, fuel_labels)

    # Input for National Emission Quotient (NEQ)
    neq = st.number_input("Enter the National Emission Quotient (NEQ) in mton CO2e:", min_value=0.0, value=0.0)
    comparison_result = compare_with_ne_quotient(total_ghg_value, neq)
    st.write(f"**{comparison_result}**")

# Run the Streamlit app
if __name__ == "__main__":
    main()
