#initially created by Matthew Rabski before creating GitHub repoitory

# List Comprehensions
# https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

info = raw_input('What is your name and age?: ')
age = [int(age) for age in info.split() if age.isdigit()]

if age > 18: print "You are allowed to drive"
else: print "You are not allowed to drive"
