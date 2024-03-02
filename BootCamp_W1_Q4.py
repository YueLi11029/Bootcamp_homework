#BootCamp_W1_Q4
# 4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
input_1 = int(input('Please input an interger: '))
input_2 = int(input('Please input another interger: '))

def sum_of_integer(a,b):
    total = a + b
    return total

output = sum_of_integer(input_1,input_2)
print('The sum of 2 integers is', output)