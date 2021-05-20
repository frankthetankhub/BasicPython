# import turtle package
from turtle import *

# two halves
for half in range(0,2):
    # if first half, color is blue, else yellow
    if half == 0:
        color('blue')
    else:
        color('yellow')
    begin_fill()
    if half == 0:
        left(180)
    else:
        left(0)
    forward(40)
    # basically a 90 degree curve
    for deg in range(0,91):
        left(1)
        forward(1)
        deg += 1
    forward(40)
    right(90)
    forward(25)
    for deg in range(0,181):
        right(1)
        forward(2)
        deg += 1
    forward(120)
    left(90)
    forward(10)
    left(90)
    forward(90)
    right(90)
    forward(25)
    for deg in range(0,181):
        right(1)
        forward(2)
        deg += 1
    forward(105)
    for deg in range(0,91):
        right(1)
        forward(1)
        deg += 1
    forward(80)
    end_fill()
    half += 1
    # back to (0,0) to start with second half
    home()
    forward(50)

# both halves are finished, now add eyes
for i in range(0,2):
    penup()
    home()
    color('white')
    if i == 0:
        left(90)
    else:
        right(90)
    forward(200)
    left(90)
    forward(50)
    pendown()
    begin_fill()
    for eye in range(0,361):
        right(1)
        forward(0.25)
        eye += 1
    end_fill()

# logo is done, wait for input
print("Nicht schön, aber selten!")
input()
