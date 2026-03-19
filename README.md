# artificial-greenhouse

# Addium AI AgTech Internship Project

This project provides tools for generating, exploring, and analyzing artifical greenhouse environmental data using Python and the Anthropic Claude API. API KEY NOT INCLUDED. Please create .env file and put your own API key there as ANTHROPIC_API_KEY="your_key_here"

# Features

- **Data Generation:**  
  Generate synthetic greenhouse data at customizable intervals (default: every 15 minutes) with modifiable bounds for each variable.

- **Data Exploration:**  
  Visualize each environmental factor without Claude API use.

- **AI Analysis:**  
  Use the Anthropic Claude API to analyze CSV data and generate concise recommendations and insights.

## Project Structure

- `data_generator.py` - Generates synthetic greenhouse data as a CSV file.
- `data_explorer.py` - Reads the CSV, converts timestamps, and creates time series plots for each variable.
- `date_time_csv_conversion.py` - Converts `%time` column to readable date/time and saves a new CSV.
- `agro_report.py` — Sends data to the Anthropic API for analysis and saves the response to a text file.
- 
- `example_greenhouse_data.csv` - Example NON-GENERATED data file, taken and modified from https://www.kaggle.com/datasets/piantic/autonomous-greenhouse-challengeagc-2nd-2019
- `generated_greenhouse_data.csv` - Output csv generated from data_generator.py
- 
- `greenhouse_report.txt` - Most recent response from agro_report.py

## Data Types

- `Tair` - temperature of air in greenhouse (°C)
- `Rhair` - relative humidity of air in greenhouse (%)
- `Cum_irr` - cumulative irrigation received throughout the day, resets at end of day (L/m^2)
- `EC_drain_PC` - electrical conductivity of drainage water (dS/m)
- `pH_drain_PC` - pH of drainage water (pH)
- `Tot_PAR` - PAR from all sources of light (micromol/m^2 s)

## Requirements

- Python 3.8+
- `pandas`
- `numpy`
- `matplotlib`
- `python-dotenv`
- `anthropic` (Claude API client)

Install dependencies with:
```
pip install pandas numpy matplotlib python-dotenv anthropic
```


© 2026 Greenhouse Data
