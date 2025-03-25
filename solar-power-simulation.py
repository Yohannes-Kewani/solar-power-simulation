import numpy as np

def solar_power_simulation(solar_irradiance, panel_area, efficiency, hours_of_sunlight):
    """
    Calculate solar panel power output.
    
    Parameters:
    solar_irradiance (float): Solar power per unit area (W/m^2)
    panel_area (float): Total panel area in square meters (m^2)
    efficiency (float): Panel efficiency as a decimal (e.g., 0.2 for 20%)
    hours_of_sunlight (float): Daily sunlight hours
    
    Returns:
    float: Total energy output per day in kWh
    """
    power_output = solar_irradiance * panel_area * efficiency  # Watts
    energy_output = power_output * hours_of_sunlight / 1000  # Convert to kWh
    return energy_output

# Example Parameters
solar_irradiance = 1000  # W/m^2 (Standard Test Condition value)
panel_area = 1.6  # m^2 (Typical solar panel size)
efficiency = 0.2  # 20% efficiency
hours_of_sunlight = 5  # Average daily sunlight hours

# Run Simulation
total_energy = solar_power_simulation(solar_irradiance, panel_area, efficiency, hours_of_sunlight)
print(f"Estimated daily energy output: {total_energy:.2f} kWh")