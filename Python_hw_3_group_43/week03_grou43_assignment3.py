### Assignment 3

## 3.1 Regular n-gons

# import necessary packages
from turtle import *

# 1.

def draw_square(sidelength):
    """ Function for drawing a square.

    Arguments:
    sidelength -- length of each side.
    """
    # go forward with given sidelength and turn 90 degrees 4 times
    for i in range(4):
        forward(sidelength)
        right(90)


# 2.

def compute_turn_angle(n):
    """ Function for computing the angle by which to return for a given n.

    Arguments:
    n -- number of corners of an n-gon.
    """
    # angle computation
    angle = 180 - ((180 * (n - 2))/n)
    return angle

# 3.

def draw_ngon(n, sidelength=100):
    """ Function for drawing an n-gon.

    Arguments:
    n -- number of corners of the n-gon.
    sidelength -- length of each side.
    """
    # go forward with given sidelength and turn the proper angle depending on n
    for i in range(n):
        forward(sidelength)
        right(compute_turn_angle(n))

# testing the function
#draw_ngon(5)
#draw_ngon(10)
#draw_ngon(7)
#draw_ngon(4)

# set-up
speed(1000)
penup()
goto(-50, 250)
pendown()

# a little fun/art
for i in range(3,20):
    draw_ngon(i)


## 3.2 Prime number checker

# 1.

def is_prime(n):
    """ Function for checking for a prime number.

    Arguments:
    n -- the number to be checked.
    """
    # 0 and 1 are no prime numbers (excluding negative numbers here)
    if n <= 1:
        return False
    else:
        # divide our number n by every int up to n
        for denominator in range(2, n):
            # if there is a divison that has remainder 0, n is no prime number
            if n % denominator == 0:
                return False
    # if there is no such number, n is only divisible by itself and 1, thus a prime number
    return True

# 2.

# Get user input n for checking prime numbers.
n = int(input("Until which number do you want to check for prime numbers? "))

# check for every number up to n whether it is prime and print the answer
for i in range(1, n+1):
    if is_prime(i):
        print(i, "is prime.")
    else:
        print(i, "is not prime.")
