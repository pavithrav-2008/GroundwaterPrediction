import numpy as np
import pandas as pd

np.random.seed(42)

n = 2000

rainfall = np.random.uniform(0, 500, n)
temperature = np.random.uniform(15, 45, n)
humidity = np.random.uniform(20, 100, n)
soil_moisture = np.random.uniform(5, 80, n)
previous_gwl = np.random.uniform(2, 30, n)
water_consumption = np.random.uniform(100, 1000, n)
recharge = np.random.uniform(0, 150, n)

noise = np.random.normal(0, 1.2, n)

groundwater_level = (
    0.35 * previous_gwl
    + 0.015 * rainfall
    + 0.08 * soil_moisture
    + 0.04 * recharge
    - 0.05 * temperature
    - 0.004 * water_consumption
    + noise
)

groundwater_level = np.clip(groundwater_level, 2, 30)

df = pd.DataFrame({
    "Rainfall": rainfall.round(2),
    "Temperature": temperature.round(2),
    "Humidity": humidity.round(2),
    "Soil_Moisture": soil_moisture.round(2),
    "Previous_Groundwater_Level": previous_gwl.round(2),
    "Water_Consumption": water_consumption.round(2),
    "Groundwater_Recharge": recharge.round(2),
    "Groundwater_Level": groundwater_level.round(2)
})

df.to_csv("groundwater_dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
print(f"\nTotal records: {len(df)}")