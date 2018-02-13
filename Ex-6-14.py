# CHAPTER 6:
# 6.14 exercises

# 1 - Write a while loop that starts at the last character in the string and works its way backwards to the
# first character in the string, printing each letter on a separate line, except backwards.
print('ex 1')
fruit = 'strawberry'
index = len(fruit)-1
while index >= 0:
    spelling = fruit[index]
    print(spelling)
    index = index - 1

#Another way to write a traversal is with a for loop:
fruit = 'pear'
for char in fruit:
    print(char)

# 2 - Given that fruit is a string, what does fruit[:] mean?
print('ex 2')
fruit = 'apple'
print(fruit[:])

# it prints the whole string

# 3 - Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.
print('ex 3')
def count(word,letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print(count)

character_count = count('potato','o')

# 4 - There is a string method called count that is similar to the function in the
# previous exercise. Read the documentation of this method at
# https://docs.python.org/3.5/library/stdtypes.html#string-methods and
# write an invocation that counts the number of times the letter a occurs in “banana”.
print('ex 4')
fruit = 'banana'
char_count = fruit.count('n')
print(char_count)

# 5 - Take the following Python code that stores a string:‘
str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a
# floating point number.
start = str.find(':')
code = float(str[start+1:])
print(code)

# 6 - Read the documentation of the string methods at
#https://docs.python.org/3.5/library/stdtypes.html#string-methods
#You might want to experiment with some of them to make sure you understand how
# they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing.
# For example, in find(sub[, start[, end]]), the brackets indicate optional arguments.
# So sub is required, but start is optional, and if you include start,
# then end is optional.