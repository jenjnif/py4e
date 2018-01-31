# exercises from chapter 1 are word answers, not programs so they
# have not been recorded on git


#3.11 exercises
# 1 - Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input('Enter Hours: '))
rate = float(input('Enter rate: '))
if hours > 40:
    overtime_hours = hours - 40
    overtime_rate = 1.5*rate
    overtime_pay = overtime_hours*overtime_rate
    gross_pay = (40*rate) + overtime_pay
else:
    gross_pay = hours * rate
print('Pay: ' + str(gross_pay))

# example input:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# 2 - Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
# by printing a message and exiting the program. The following shows two executions of the program:

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter rate: '))
except:
    print('Error, please enter numeric input')
    exit()
if hours > 40:
    overtime_hours = hours - 40
    overtime_rate = 1.5*rate
    overtime_pay = overtime_hours*overtime_rate
    gross_pay = (40*rate) + overtime_pay
    print('Pay: ' + str(gross_pay))
else:
    gross_pay = hours * rate
    print('Pay: ' + str(gross_pay))

# example input:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input


# 3 - Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an
# error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score
# >= 0.9   A
# >= 0.8   B
# >= 0.7   C
# >= 0.6   D
# <0.6     F

# Enter score: 0.95
# A

# Enter score: perfect
# Bad score

# Enter score: 10.0
# Bad score

# Enter score: 0.75
# C

# Enter score: 0.5
# F

# Run the program repeatedly as shown above to test the various different values for input.

try:
    score = float(input('Please enter a score between 0.0 and 1.0:\n'))
except:
    print('Bad Score')
    exit()
if score < 0.0 or score > 1.0:
    print('Bad score')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
else:
    print('Bad Score')









