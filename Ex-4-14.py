# CHAPTER 4:

# 4.14 exercises

# 1 - Run the program on your system and see what numbers you get. Run the program more than once and see what
# numbers you get.

# import random or import math - creates a module object named random/math
import random
for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

# This program produces the following list of 10 random numbers between 0.0 and up to but not including 1.0.

# 2 - Move the last line of this program to the top, so the function call appears before the definitions.
# Run the program and see what error message you get.

# repeat_lyrics() # Produces this error message: NameError: name 'repeat_lyrics' is not defined

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# 3 - Move the function call back to the bottom and move the definition of print_lyrics after the definition of
# repeat_lyrics. What happens when you run this program?


def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

# it still works as both functions have been defined before repeat_lyrics is called


# 4 - Exercise 4: What is the purpose of the “def” keyword in Python?
# b) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true - this one!

# 5 - What will the following Python program print out?
def fred():
    print("Zap")

def jane():
   print("ABC")
jane()
fred()
jane()

# d) ABC Zap ABC - this one


# 6 - Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay
# which takes two parameters (hours and rate).

def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            overtime_hours = hours - 40
            overtime_rate = 1.5 * rate
            overtime_pay = overtime_hours * overtime_rate
            gross_pay = (40 * rate) + overtime_pay
            return (gross_pay)
        else:
            gross_pay = hours * rate
            return (gross_pay)
    except:
        return('Error, please enter numeric input')

hours_input = input('Enter Hours: ')
rate_input = input('Enter rate: ')

gross_pay = computepay(hours_input,rate_input)
print(gross_pay)

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# 7 - Rewrite the grade program from the previous chapter using a function called computegrade that
# takes a score as its parameter and returns a grade as a string.

# >0.9    A
# >0.8    B
# >0.7    C
# >0.6    D
# <= 0.6  F


def computegrade(score):
    try:
        score = float(score)
        if score < 0.0 or score > 1.0:
            return('Bad score')
        elif score >= 0.9:
            return('A')
        elif score >= 0.8:
            return('B')
        elif score >= 0.7:
            return('C')
        elif score >= 0.6:
            return('D')
        else:
            return('F')
    except:
        return ('Bad Score')


score_input = input('Please enter a score between 0.0 and 1.0:\n')
grade = computegrade(score_input)
print(grade)

# Program Execution:
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