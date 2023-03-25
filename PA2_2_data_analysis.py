import pandas as pd
import numpy as np

data = pd.read_csv('US_Crime_Rates_1960_2014.csv')
arguments = input()
arguments = arguments.split()
arguments = np.array(arguments)
arguments = arguments.astype(np.float64)
arguments = np.round(arguments)
data_new = data.iloc[:, 3:]

# These codes below may use many methods and function referred to CSDN.
data_group_by_decade = data_new.groupby(data_new.index // 10).sum()
sums_by_decade = data_group_by_decade.dot(arguments)
crime_points = pd.DataFrame({'Crime_Points': sums_by_decade})

population = data.iloc[9::10, 1]
population = population.reset_index(drop=True)
population.loc[5] = data.iloc[54, 1]
crime_points.insert(0, 'Population', population)
year = pd.Series(['1960-01-01', '1970-01-01', '1980-01-01', '1990-01-01', '2000-01-01', '2010-01-01'], name = 'Year')
crime_points = crime_points.set_index(year)
crime_points_sorted = crime_points.sort_values(by='Crime_Points', ascending=False)
crime_points_sorted['Crime_Points'] = pd.to_numeric(crime_points_sorted['Crime_Points'], downcast='integer')
crime_points_sorted['Population'] = pd.to_numeric(crime_points_sorted['Population'], downcast='integer')
print(crime_points_sorted)