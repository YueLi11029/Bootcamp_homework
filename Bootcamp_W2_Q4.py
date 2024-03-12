#question4
'''
4)Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape this array into two separate
2D arrays, where one represents the rows and the other represents the columns. Write a function, preferably using a
lambda function, to calculate the sum of each row and each column separately, and return the results as two separate
NumPy arrays

'''

import numpy as np
import random

array = np.random.randint(1,100,size=(4,4))

rows = array.reshape(2, 8).copy()
columns = array.reshape(8, 2).copy()


#print(array)
#print(rows)
#print(columns)

def sum_rows(num):
    return np.array([np.sum(row) for row in rows])

# Define a function to calculate the sum of columns
def sum_columns(num):
    return np.array([np.sum(column) for column in columns])

# Calculate the sums of rows and columns using the defined functions
sum_of_rows = sum_rows(rows)
sum_of_columns = sum_columns(columns)


print('Original array:')
print(array)

print('\nSums of rows:')
print(sum_of_rows)
print('\nSums of columns:')
print(sum_of_columns)

