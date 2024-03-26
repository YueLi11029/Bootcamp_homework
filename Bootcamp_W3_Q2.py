import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
2) Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions influence pedestrian activity in that year. Sort the pedestrian count data by weather summary to identify any correlations( with a correlation matrix) between weather patterns and pedestrian counts for the selected year.
'''
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
data = pd.read_csv(url)

brooklyn_bridge_data = data[(data['Hour_beginning'].dt.year == 2019) & (data['location'] == 'Brooklyn Bridge')]

correlation_matrix = brooklyn_bridge_data[['Pedestrians', 'Weather Summary']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix: Weather Summary vs Pedestrian Counts (Brooklyn Bridge, 2019)')
plt.show()
