# Assignment 1: Interchanging loops

## 1.
some_number = 42

# print the numbers from 42 to 99
for some_number in range(some_number,100):
    print("Look at my number:", some_number)

## 2.
some_number = 42
counter = 0

# print some_number minus 2 times the loop count until it is not greater than -48
while some_number > -48:
    some_number -= 10 + counter * 2
    print(some_number)
    counter += 1
