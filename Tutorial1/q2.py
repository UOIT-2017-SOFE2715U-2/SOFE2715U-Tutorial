info = raw_input('What is your name and age?: ')
[int(age) for age in info.split() if age.isdigit()]
age = int(age)
if age > 18: print "You are allowed to drive"
else: print "You are not allowed to drive"

