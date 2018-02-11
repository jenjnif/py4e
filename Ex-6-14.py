# CHAPTER 6:

# 6.14 exercises

# 1 - Write a while loop that starts at the last character in the string and works its way backwards to the
# first character in the string, printing each letter on a separate line, except backwards.

fruit = "strawberry"
index = len(fruit)-1
while index >= 0:
    spelling = fruit[index]
    print(spelling)
    index = index - 1

#Another way to write a traversal is with a for loop:
fruit = "pear"
for char in fruit:
    print(char)

# 2 - Given that fruit is a string, what does fruit[:] mean?
fruit = "apple"
print(fruit[:])

# it prints the whole string

# 3 - Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.


def count(word,letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print(count)

character_count = count("potato","o")

# 4 - There is a string method called count that is similar to the function in the
# previous exercise. Read the documentation of this method at
# https://docs.python.org/3.5/library/stdtypes.html#string-methods and
# write an invocation that counts the number of times the letter a occurs in “banana”.

