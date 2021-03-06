# CHAPTER 5:

# 5.10 exercises

# 1 - Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number,
# detect their mistake
#
# total = 0
# count = 0
# average = 0
#
# while True:
#     number = input("Enter a number: ")
#     try:
#         number_input = float(number)
#     except Exception as e:
#         if number == 'done':
#             print(total, count, average)
#             exit()
#         else:
#             print("Invalid input")
#             continue
#     total = total + number_input
#     count = count + 1
#     average = total / count


# using try and except and print an error message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333


# 2 - Write another program that prompts for a list of numbers as above and at the end prints out both the maximum
# and minimum of the numbers instead of the average.

total = 0
count = 0
smallest = None
biggest = None


while True:
    number = input("Enter a number: ")
    try:
        number_input = int(number)
    except Exception as e:
        if number == 'done':
            print('total is ',total,'count is ',count, 'biggest is ',biggest, 'smallest is ',smallest)
            exit()
        else:
            print("Invalid input")
            continue
    if smallest is None or number_input < smallest:
        smallest = number_input
        print('Smallest number so far is ' + str(number_input))
    if biggest is None or number_input > biggest:
        biggest = number_input
        print('Biggest number so far is: ' + str(number_input))
    total = total + number_input
    count = count + 1