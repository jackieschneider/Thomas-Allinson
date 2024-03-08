!pip install wbdata
!pip install --upgrade wbdata
!pip insatll matplotlib

import wbdata
import pandas as pd
import matplotlib.pyplot as plt

# Set the indicator code for life expectancy
indicator_code = 'SP.DYN.LE00.IN'

# List of countries (optional, you can omit this list to include all countries)
countries = ['USA', 'CRI', 'ITA', 'GRC', 'JPN']

# Fetch life expectancy data directly from wbdata
data = wbdata.get_dataframe(indicators={indicator_code: "Life Expectancy"}, country=countries, convert_date=True)

# Filter data for the time period from 2000 to 2024
data = data[data.index.get_level_values("date").year >= 2000]

# Pivot the data to have countries as columns and years as indices
df_pivot = data.pivot_table(values='Life Expectancy', index=data.index.get_level_values("date"), columns='country')

# Calculate the average life expectancy for each year
df_pivot['average'] = df_pivot.mean(axis=1)

# Calculate the international average life expectancy for each year
international_average = df_pivot.mean(axis=1)

# Plotting
plt.figure(figsize=(12, 8.87))
for country in df_pivot.columns[:-1]:  # Exclude the 'average' column
    plt.plot(df_pivot.index, df_pivot[country], marker='o', label=country)

plt.plot(df_pivot.index, international_average, color='black', linestyle='dashdot', linewidth=2, label='World Average Life Expectancy')
plt.title('Average Life Expectancy')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.legend()
plt.grid(True)
plt.show()
