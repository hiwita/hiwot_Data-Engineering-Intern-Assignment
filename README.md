# hiwot_Data-Engineering-Intern-Assignment
# Weather Data Processing Pipeline

## Overview

This project demonstrates a basic data ingestion, cleaning, transformation, and output workflow using Python and Pandas on weather data. The goal is to process a CSV file containing weather observations, clean and transform the data, and save the results for further analysis.

---

## Project Structure

- `weather_data.csv` — Original raw weather data CSV file.  
- `HiwotTadesse.py` — Python script containing the data processing code.
- `outputs/` — Folder to store output files including cleaned CSV and reports.  
- `tranformed_weather_data.csv` - Output clean data
---

## Data Description

The input CSV file `weather_data.csv` contains weather data with the following columns:

| Column              | Description                          |
|---------------------|------------------------------------|
| date                | Date of observation (varied format)|
| city                | City name                          |
| temperature_celsius | Temperature in Celsius             |
| humidity_percent    | Relative humidity (%)              |
| wind_speed_kph      | Wind speed in kilometers per hour |
| weather_condition   | Weather condition description     |

---

## Steps

### 1. Data Ingestion

- Load `weather_data.csv` into a Pandas DataFrame using Python.

### 2. Data Cleaning and Transformation

- **Handle Missing Values:**  
  - Replace missing `temperature_celsius`, `humidity_percent`, `wind_speed_kph` values with the average temperature for that city.  
  - Drop rows where `date` is missing.

- **Standardize Dates:**  
  - Convert the `date` column into a consistent `YYYY-MM-DD` format.

- **Add a New Column:**  
  - Create `temperature_fahrenheit` by converting Celsius to Fahrenheit using the formula:  
    F = C × 9/5 + 32

- **Filter Data:**  
  - Remove rows where `weather_condition` is "Unknown" or null.

### 3. Data Output

- Save the cleaned and transformed data (including `temperature_fahrenheit`) as `outputs/transformed_weather_data.csv`.

- Optional: Generate a text or markdown report listing the top 5 cities with the highest average temperature in Celsius.

---

## How to Run

1. Ensure Python 3.x and Pandas are installed: `import pandas as pd`

2. Place `weather_data.csv` in the working directory.

3. Run the processing script (if provided):

4. Check the `outputs/` folder for:

- `transformed_weather_data.csv` — Cleaned and transformed data.

---

## Notes

- Make sure the input CSV `weather_data.csv` is attached or placed alongside this README before running the pipeline.
- The `outputs/` folder will be created automatically if it does not exist.
- The project can be extended to include more sophisticated analysis or visualization.



