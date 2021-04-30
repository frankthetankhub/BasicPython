### Assignment 4

# import necessary packages
from random import randint

# get string length by user input
length = int(input("How long should your random string be? "))

for i in range (0, length):
    # get random integer between 1 and 10; used as probability
    prob = randint(1,10)

    if prob <= 7:
        print("X", end="")
    else:
        print("O", end="")
    i += 1
