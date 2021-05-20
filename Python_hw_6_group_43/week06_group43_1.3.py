# Assignment 1: Warm-up
## 1.3 Plotting

# import necessary modules
from matplotlib import pyplot as plt

# data for x axis
list_of_numbers = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
plt.plot(list_of_numbers, [x**2 for x in list_of_numbers])
plt.show()
