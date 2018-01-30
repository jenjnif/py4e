# exercises from chapter 1 are word answers, not programs so they
# have not been recorded on git


#2.15 exercises
# 2 - Write a program that uses input to prompt a user for their name and then welcomes them.
name = input('Enter your name\n')
print('Hello ' + name)

# 3 - Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = float(input('Enter Hours: '))
rate = float(input('Enter rate: '))
gross_pay = hours*rate
print('Pay: ' + str(gross_pay))

# 4 - Assume that we execute the following assignment statements:

width = 17
height = 12.0

# For each of the following expressions, write the value of the expression
# and the type (of the value of the expression).
# 1. width//2
one = width//2
print(one)
print(type(one))

# 2. width/2.0
two = width/2.0
print(two)
print(type(two))

# 3. height/3
three = height/3
print(three)
print(type(three))

# 4. 1 + 2 * 5
four = 1 + 2 * 5
print(four)
print(type(four))

# Use the Python interpreter to check your answers.

# 5 - Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
# and print out the converted temperature.

celsius = float(input('Celsius temperature'))
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)