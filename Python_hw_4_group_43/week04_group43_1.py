# Assignment 1.1 while

user_input = ""
# loop until the user input equals string "exit"
while user_input != "exit":
    # Get user input
    user_input = input("Please enter something: ")

# Assignment 1.2 randint and print

# import necessary packages
from random import randint

# for 100 steps, get random integer and concatenate to printed string
for i in range(100):
    random_number = randint(0,9)
    print(str(random_number), end="")

print("\n")

# Assignment 1.3 type

# loop until termination in console: ask for input and print data type
while True:
    i = input("Please enter something: ")
    print(type(i))

# the type will always be a string
