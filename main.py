'''
Exercise 4b

Write a program that asks the user for their name and then produces a “name
triangle”: the first letter of their name, then the first two letters, then the first
three, and so forth, until the entire name is written on the final line.

'''

name = input('Enter your name: ')
counter = 1
for letter in name:
    print(name[:counter])
    counter += 1