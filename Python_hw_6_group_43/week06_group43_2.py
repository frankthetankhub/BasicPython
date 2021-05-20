# Assignment 2
# 1.

def print_n_lines(filename, n):
    """
    Function that prints the last n lines of a text file.

    Args:
    - filename: the name of the file which should be read from
    - n: number of lines that should be printed
    """

    # open file with given filename, read and print all specified lines
    with open(filename, "r") as text:
        text = text.read().splitlines()
        for line in text[-n:]:
            print(line)


# test the function: print 7 and 15 last lines from poem
print_n_lines("06_my_shadow.txt", 7)
print_n_lines("06_my_shadow.txt", 15)

# 2.

# open distances file, read and split every line
with open("06_2_distances.txt", "r") as distances:
    result = 0
    # for each line, split into list, get first element,
    # convert if necessary, cast to float and sum up the result
    for d in distances:
        d = d.split()
        if d[1] == "cm":
            value = float(d[0]) / 100
        elif d[1] == "mm":
            value = float(d[0]) / 1000
        else:
            value = float(d[0])

        # 4. write distances > 50m to a new file
        if value > 50:
            with open("greater_50.txt", "a") as distances_50:
                print(value, file=distances_50)
        result += value
    print(result)

# 3.

# create new text file and write the result from above into it
with open("total_distance.txt", "w") as total_distance:
    print(result, file=total_distance)
