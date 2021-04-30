### Assignment 2.2

# Get user input for dimensions of grid
n = int(input("Give a number n for the n x n divisibility table: "))

for row in range(n+1):
    for column in range(n+1):
        # if in first row (row = 0) print the column numbers
        if row == 0:
            if column == 0:
                pass
            else:
                print("   " + str(column), end="")
        else:
            if column == 0:
                print(str(row) + "  ", end="")
            else:
                if column % row == 0:
                    print("X   ", end="")
                    #print("col:", column, "row:", row)
                else:
                    print("    ", end="")
    # print a new line for each new row
    print("\n")
