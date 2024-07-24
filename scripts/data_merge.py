# -*- coding: utf-8 -*-
"""
data_merge.py
Description:
This script processes and merges multiple datasets related to COVID-19 vaccinations, 
infection statistics, and population data. 
    
@author: Carlos A. Duran-Villalobos
"""
import pandas as pd

# Load the datasets
vaccinations = pd.read_csv('../data/country_vaccinations.csv')
vaccinations_by_manufacturer = pd.read_csv('../data/country_vaccinations_by_manufacturer.csv')
worldometer = pd.read_csv('../data/worldometer_coronavirus_daily_data.csv')
population = pd.read_csv('../data/world_population.csv')

# Display the first few rows of each dataset
print("Vaccinations Data:")
print(vaccinations.head())

print("\nVaccinations by Manufacturer Data:")
print(vaccinations_by_manufacturer.head())

print("\nWorldometer Data:")
print(worldometer.head())

print("\nPopulation Data (before processing):")
print(population.head())

# Display the column names to understand the structure of each dataset
print("\nVaccinations Columns:", vaccinations.columns)
print("\nVaccinations by Manufacturer Columns:", vaccinations_by_manufacturer.columns)
print("\nWorldometer Columns:", worldometer.columns)
print("\nPopulation Columns:", population.columns)

# Ensure date formats are consistent
vaccinations['date'] = pd.to_datetime(vaccinations['date'])
vaccinations_by_manufacturer['date'] = pd.to_datetime(vaccinations_by_manufacturer['date'])
worldometer['date'] = pd.to_datetime(worldometer['date'])

# Standardize the country names to uppercase
vaccinations['country'] = vaccinations['country'].str.upper()
vaccinations_by_manufacturer['location'] = vaccinations_by_manufacturer['location'].str.upper()
worldometer['country'] = worldometer['country'].str.upper()
population = population.rename(columns={'Country/Territory': 'country', '2022 Population': 'population'})
population['country'] = population['country'].str.upper()

# Keep only the country and 2022 population columns in the population data
population = population[['country', 'population']]

print("\nPopulation Data (after processing):")
print(population.head())

# Merge vaccinations and worldometer datasets on country and date
merged_data = pd.merge(vaccinations, worldometer, on=['country', 'date'], how='outer')

# Merge the result with population data
merged_data = pd.merge(merged_data, population, on='country', how='left')

# Aggregate the vaccinations_by_manufacturer data by country and sum the total_vaccinations
vaccinations_by_manufacturer_agg = vaccinations_by_manufacturer.groupby(['location', 'vaccine']).agg({'total_vaccinations': 'sum'}).reset_index()
vaccinations_by_manufacturer_agg = vaccinations_by_manufacturer_agg.rename(columns={'location': 'country'})
vaccinations_by_manufacturer_agg['country'] = vaccinations_by_manufacturer_agg['country'].str.upper()

# Merge the aggregated manufacturer data with the merged dataset
final_data = pd.merge(merged_data, vaccinations_by_manufacturer_agg, on='country', how='outer')

# Drop the CCA3 column if it exists
if 'CCA3' in final_data.columns:
    final_data = final_data.drop(columns=['CCA3'])

# Save the final merged dataset
final_data.to_csv('../data/cleaned_covid_combined_data.csv', index=False)
