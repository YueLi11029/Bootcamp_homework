'''
Work on the Brooklyn Pedestrian Dataset: https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD

1)Filter the data to include only weekdays (Monday to Friday) and plot a line
graph showing the pedestrian counts for each day of the week.

'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = '/Users/liyue/Desktop/Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project.csv'
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['weekday'] = df['hour_beginning'].dt.dayofweek

weekdays_df = df[df['weekday'].isin([0, 1, 2, 3, 4])]

pedestrian_counts_per_day = weekdays_df.groupby(weekdays_df['hour_beginning'].dt.day_name())['pedestrian_count'].sum()


plt.figure(figsize=(10, 6))
pedestrian_counts_per_day.plot(kind='line', marker='o')
plt.title('Pedestrian Counts on Weekdays')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Counts')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

