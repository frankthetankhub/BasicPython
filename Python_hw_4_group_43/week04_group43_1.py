# Task 4.1 - Warm-up exercises
## Task 4.1.1 - while
inp = ""
### loop until the users input is "exit"
while inp != "exit":
    ### get input from user
    inp = input("Please enter something: \n")

## Task 4.1.2 - randint and print
### import necessary method from package random
from random import randint
### loop for 100 iterations
for i in range(100):
    ### choose random number between 0 and 9
    random = randint(0,9)
    ### and print and the chosen numbers in the same row
    print(random, end = '')
print("\n")

## Task 4.1.3 - type
### loop until termination via console
while True:
    inp = input("Please write something: \n")
    print(type(inp))
# observation: the typed input given by the user is always of type string (even when nothing is entered at all)
