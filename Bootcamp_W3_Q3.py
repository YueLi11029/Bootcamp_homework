import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
3) Implement a custom function to categorize time of day into morning, afternoon, evening, and night, and create a new column in the DataFrame to store these categories. Use this new column to analyze pedestrian activity patterns throughout the day.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
data = pd.read_csv(url)

def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

data['Time of Day'] = data['Hour'].apply(categorize_time_of_day)
time_of_day_counts = data.groupby('Time of Day')['Pedestrians'].sum()
plt.figure(figsize=(8, 6))
time_of_day_counts.plot(kind='bar', color='skyblue')
plt.title('Pedestrian Activity Patterns Throughout the Day')
plt.xlabel('Time of Day')
plt.ylabel('Pedestrian Counts')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
