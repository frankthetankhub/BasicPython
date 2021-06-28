#Task 10.1 - Factorial
#10.1.1 - Recursive definition
""" The base case would be fac(0) = 1 and you can calculate the factorial recursively by multiplying the factorial before with the current number so:
fac(n) = fac(n-1)*n. """
#10.1.2 - recursive program
def factorial(int):
    # check for negative integer
    if int < 0:
        print(f"Given integer: {int} is negative, please choose a non-negative integer")
        return
    # base case
    if int == 0:
        return 1
    # recursive definition
    return factorial(int-1)*int
