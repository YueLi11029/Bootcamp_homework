#BootCamp_W1_Q3
# Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for number in range (1,21):
    if number % 2 == 0:
        print(number,'is an even number')
    else:
        print(number,'is an odd number')