# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
# Data ingestion
df = pd.read_csv("weather_data.csv")

# Replacing the nan by the mean of temperature, humidity and wind speed 
# for that city
cols = ['temperature_celsius', 'humidity_percent','wind_speed_kph']
for col in cols:
    df[col] = df[col].fillna(df.groupby('city')[col].transform('mean'))

# drop the nan date
df = df.dropna(subset=['date'])

#  Standardizing Dates
df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')

# Add a New Column: Create a temperature_fahrenheit column by converting 
# temperature_celsius using the formula: F=C×9/5+32
df["temperature_fahrenheit"] = (df["temperature_celsius"]*9/5)+32

# Filter Data: Keep only rows where weather_condition is not 
# "Unknown" or null.
df_filtered = df[(df['weather_condition'].notna()) & (df['weather_condition'] != 'Unknown')]

# Data Output
df_filtered.to_csv("outputs/tranformed_weather_data.csv")

# Bonus (Optional)
# Generate a simple text report (e.g., Markdown or TXT file) listing 
# the top 5 cities with the highest average temperature_celsius
df_filtered.groupby("city")["temperature_celsius"].mean()