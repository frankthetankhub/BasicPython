#Task 4. Bonus Task: Socially distancing Prime Numbers
# libraries
import matplotlib.pyplot as plt
import numpy as np

# create lists for the prime numbers and their distances
prime_distances = []
prime_numbers = []
# create current as all the numbers to be checked starting with 2 as the first prime number
current = 2

# create a method which returns a boolean value for a given number if the given number is a prime number or not
def is_prime(number):
    # check for prime numbers via trial division
    for p in prime_numbers:
        # condition of trial division which found prime numbers need to be considered
        if 2 <= p <= np.sqrt(number):
            # if the number to be checked can be divided by another prime number
            if number%p == 0:
                # checked number is not a prime number
                return False
        # break condition to decrease runtime in combination with condition of trial division for which prime numbers need to be considered for the division
        else:
            break
    # if the trial division was unsuccessful the checked number is a prime number
    return True

# while condition for all prime numbers up to 100000
while current <= 100000:
    # if the currently viewed number is a prime number it is appended to the found prime numbers
    if is_prime(current):
        prime_numbers.append(current)
    # current increases to check the next number
    current += 1

# calculate the distance between all prime numbers as their difference
for i in range(len(prime_numbers)-1):
    prime_distances.append(prime_numbers[i+1]-prime_numbers[i])

# based on the plot bigger prime numbers are more likely to social distance

# plot prime distances
plt.plot(np.convolve(prime_distances, np.ones(1000)/1000, mode="valid"))
plt.xticks([])
plt.yticks([])
plt.xlabel("primes")
plt.ylabel("averaged distance")
plt.show()
