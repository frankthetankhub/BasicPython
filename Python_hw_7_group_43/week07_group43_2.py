# Task 7.2 - Debugging
## Task 7.2.1 - Calculating the Average
def read_n_values(n):
    print("Please enter", n, "values.")
    values = []

    for i in range(n):
        values.append(input("Value {}: ".format(i + 1)))
    return values


def compute_average(values):
    # set sum to first value of list
    total_sum = int(values[0])                              ### added int() here


    # iterate over remaining values and add them up
    for value in values[1:]:
        print(f"this is value: {value}")
        total_sum += int(value)                             ### added int() here
        print(f"this is total sum: {total_sum}")

    return float(total_sum) / len(values)

values = read_n_values(3)
print("Average:", compute_average(values))
### wrong output for values = [7,7,7] is 259.0 instead of 7.0
### problem: the inputs in "values" in this case are all strings and not integers so when using total_sum += value, value is a string containing one number, so the total_sum for values[7,7,7] is "777" instead of 21
### fix: pull the numbers from the list "values", which are strings, as integers by adding int() to line 12 and 16 to compute total_sum correctly

##Task 7.2.2 - The Best Colors
def write_to_file(string, filename):
    """function for writing a string to a file"""
    with open(filename, "a") as f:                          ### changed "w" to "a" here
        f.write(string)

template    = "{} is the best color\n"                      ### added \n here
colors      = ["light blue", "sky blue", "ocean blue", "navy blue", "dark blue"]

# write a line for each color to the file
for color in colors:
    write_to_file(template.format(color), "best_colors.txt")

### wrong content of best_colors.txt is "dark blue is the best color" instead of all colors included in "colors", so "light blue", "sky blue", "ocean blue" and "navy blue" are missing
### problem: in line 3 the second argument of open() should not be "w" because this will overwrite anything in "best_colors.txt" so only the last entry, which is dark blue will remain in the end
### fix: use "a" for append in line 3 as the second argument of open() to keep the previously added lines in "best_colors.txt"
### contents of best_colors.txt after running the code:
###                                                     light blue is the best colorsky blue is the best colorocean blue is the best colornavy blue is the best colordark blue is the best color
                                               
### problem 2: when using "a" instead of "w" the programm will print the templates all in the same line
### fix 2: added "\n" to the template in line 6 to guarantee a new line after each template
### contents of best_colors.txt after running the code:
###                                                     light blue is the best color
###                                                     sky blue is the best color
###                                                     ocean blue is the best color
###                                                     navy blue is the best color
###                                                     dark blue is the best color
