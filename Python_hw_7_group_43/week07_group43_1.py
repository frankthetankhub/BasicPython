# Task 7.1 - Warm-up exercises
## Task 7.1.1 - Files
import numpy as np
from random import randint
### create file randomness
file = open("randomness.txt","w")
### create string for the line
line = ""
for i in range(1000):
    ### choose random number between 0 and 9
    random = randint(0,9)
    ### and add the number to the string
    line += str(random)
file.write(line)

## Task 7.1.2 - Numpy
### create the 2 arrays as told
array1 = np.array([1,2,3])
array2 = np.array([4,7,8])
### use numpy function dot() to compute dot product of the 2 arrays
dot_product = np.dot(array1, array2)
