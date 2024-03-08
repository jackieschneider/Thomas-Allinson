#The following code plots Each blue zone country. This allows us to further analyze how the countries of each blue zone differ in average life expectancy. 

!pip install wbdata
!pip install matplotlib
!pip install --upgrade wbdata



import wbdata
import pandas as pd
import matplotlib.pyplot as plt

# Set the indicator code for life expectancy
indicator_code = 'SP.DYN.LE00.IN'
countries = ['USA', 'CRI', 'ITA', 'GRC', 'JPN']

 
data = wbdata.get_dataframe(indicators={indicator_code: "Life Expectancy"}, country=countries)
data.reset_index(inplace=True)


data['date'] = pd.to_datetime(data['date'])
data = data[data['date'].dt.year >= 2000]

df_pivot = data.pivot_table(values='Life Expectancy', index='date', columns='country')

# Calculate the average life expectancy for each year
df_pivot['average'] = df_pivot.mean(axis=1)

# Calculate the international average life expectancy 
international_average = df_pivot.mean(axis=1)

plt.figure(figsize=(12, 8.87))
for country in df_pivot.columns[:-1]:  
    plt.plot(df_pivot.index, df_pivot[country], marker='o', label=country)

plt.plot(df_pivot.index, international_average, color='black', linestyle='dashdot', linewidth=2, label='World Average Life Expectancy')
plt.title('Average Life Expectancy')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.legend()
plt.grid(True)
plt.show()
