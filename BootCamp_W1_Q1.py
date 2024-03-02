#BootCamp_W1_Q1
#Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
word = input('Please enter a word: ')
vowels = ['a','e','i','o','u']


def count_vowels(word):
    count = 0
    for character in word.lower():
        if character in vowels:
            count += 1
        
    return count

print('the number of vowels in the word',word,'is:',count_vowels(word))