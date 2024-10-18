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

# Function to calculate emissions for Hydrogen and CO
def calculate_hydrogen_emissions(amount_of_hydrogen):
    emission_factor_h2 = 0  # Hydrogen combustion produces no direct CO2
    return amount_of_hydrogen * emission_factor_h2

def calculate_co_emissions(amount_of_co):
    emission_factor_co = 1.16  # kg CO per liter
    return amount_of_co * emission_factor_co

# Function to display images of gases
def display_gas_image(gas_name):
    gas_images = {
        "CO2": "https://www.example.com/co2_image.png",  # Replace with the actual image URLs
        "CH4": "https://www.example.com/ch4_image.png",
        "N2O": "https://www.example.com/n2o_image.png",
        "CO": "https://www.example.com/co_image.png",
        "H2": "https://www.example.com/h2_image.png"
    }
    image_url = gas_images.get(gas_name, None)
    if image_url:
        image = Image.open(image_url)
        st.image(image, caption=f"{gas_name} Gas")

# Function to calculate total GHG emissions in CO2 equivalents
def calculate_total_ghg(co2, ch4, n2o):
    ch4_co2e = ch4 * 25  # Convert CH4 to CO2e
    n2o_co2e = n2o * 298  # Convert N2O to CO2e
    total_ghg = (co2 + ch4_co2e + n2o_co2e) / 1000  # Convert kg to mton
    return total_ghg

# Main Streamlit app
def main():
    st.title("Greenhouse Gas Emission Calculator Dashboard")
    st.write("An interactive calculator for GHG emissions from various sources, including coal, biomass, natural gas, diesel oil, Carbon Monoxide (CO), and Hydrogen (H2).")
    
    # Sidebar for general information
    st.sidebar.header("Navigation")
    st.sidebar.markdown("""
        - **CO2, CH4, N2O** Emissions
        - **CO** Emissions
        - **H2** Emissions
    """)
    
    # Sidebar for developer credits
    st.sidebar.markdown("### Developed by")
    st.sidebar.info("Your Name | Chemical Science and AI Enthusiast")

    # Tabbed interface for different gases
    tab1, tab2, tab3 = st.tabs(["CO2, CH4, N2O", "CO", "H2"])

    # Tab 1: CO2, CH4, N2O emissions from coal, biomass, gas, diesel
    with tab1:
        st.subheader("CO2, CH4, N2O Emissions")
        amount_of_coal = st.number_input("Enter the amount of coal burned (tons):", min_value=0.0, value=0.0)
        coal_emissions = calculate_coal_emissions(amount_of_coal)
        st.write(f"CO2 emissions from coal: {coal_emissions[0]/1000:.2f} mton CO2")
        st.write(f"CH4 emissions from coal: {coal_emissions[1]/1000:.4f} mton CH4")
        st.write(f"N2O emissions from coal: {coal_emissions[2]/1000:.4f} mton N2O")
        
        # Show images for gases
        st.write("### Gas Images")
        display_gas_image("CO2")
        display_gas_image("CH4")
        display_gas_image("N2O")

    # Tab 2: Carbon Monoxide (CO) emissions
    with tab2:
        st.subheader("Carbon Monoxide (CO) Emissions")
        amount_of_co = st.number_input("Enter the amount of CO emitted (liters):", min_value=0.0, value=0.0)
        co_emissions = calculate_co_emissions(amount_of_co)
        st.write(f"CO emissions: {co_emissions:.2f} kg CO")
        
        # Show image for CO gas
        display_gas_image("CO")

    # Tab 3: Hydrogen (H2) emissions
    with tab3:
        st.subheader("Hydrogen (H2) Emissions")
        amount_of_hydrogen = st.number_input("Enter the amount of Hydrogen burned (tons):", min_value=0.0, value=0.0)
        h2_emissions = calculate_hydrogen_emissions(amount_of_hydrogen)
        st.write(f"H2 emissions: {h2_emissions:.2f} kg H2 (No direct CO2 emissions from H2 combustion)")

        # Show image for H2 gas
        display_gas_image("H2")

    # Footer
    st.markdown("### Developed by [Your Name](https://your-website.com)")

if __name__ == "__main__":
    main()
