#Task 10.2 - Sudoku
#Task 10.2.1 - Representation of the Problem
grid = [[7, 0, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]
print(grid)

#Task 10.2.2 - Printing the Grid, but nicely
def print_grid(grid):
    # counter for empty rows after every 3 rows
    rows = 0
    for row in grid:
        # print the rows in blocks of 3
        print(row[0:3], row[3:6], row[6:9])
        rows += 1
        # add empty row after every 3 rows
        if rows%3 == 0:
            print("")

#Task 10.2.3 - Solving the Sudoku - possible
def possible(row, col, d):
    for e in grid[row]:
        if e == d:
            #print("found in row")
            return False
    for rows in grid:
        if rows[col] == d:
            #print("found in collumn")
            return False
    # if (rows[col] == d for rows in grid):
    #     print("found in collumn")
    #     return False
    #upper left cell
    if (0<=row<=2 & 0<=col<=2):
        cell = []
        # take correct rows
        for rows in grid[0:3]:
            # and correct collumns
            cell.append(rows[0:3])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # middle left cell
    elif (0<=row<=2 & 3<=col<=5):
        cell = []
        # take correct rows
        for rows in grid[0:3]:
            # and correct collumns
            cell.append(rows[3:6])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # lower left cell
    elif (0<=row<=2 & 6<=col<=8):
        cell = []
        # take correct rows
        for rows in grid[0:3]:
            # and correct collumns
            cell.append(rows[6:])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # upper middle cell
    elif (3<=row<=5 & 0<=col<=2):
        cell = []
        # take correct rows
        for rows in grid[3:6]:
            # and correct collumns
            cell.append(rows[0:3])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # middle middle cell
    elif (3<=row<=5 & 3<=col<=5):
        cell = []
        # take correct rows
        for rows in grid[3:6]:
            # and correct collumns
            cell.append(rows[3:6])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # middle lower cell
    elif (3<=row<=5 & 6<=col<=8):
        cell = []
        # take correct rows
        for rows in grid[3:6]:
            # and correct collumns
            cell.append(rows[6:])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # right upper cell
    elif (6<=row<=8 & 0<=col<=2):
        cell = []
        # take correct rows
        for rows in grid[6:]:
            # and correct collumns
            cell.append(rows[0:3])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # right middle cell
    elif (6<=row<=8 & 3<=col<=5):
        cell = []
        # take correct rows
        for rows in grid[6:]:
            # and correct collumns
            cell.append(rows[3:6])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    # right lower cell
    elif (6<=row<=8 & 6<=col<=8):
        cell = []
        # take correct rows
        for rows in grid[6:]:
            # and correct collumns
            cell.append(rows[6:])
        # check in all elements in the cell for the number to try
        for rows in cell:
            for e in rows:
                if e == d:
                    #print("found in cell")
                    return False
    return True

# Task 10.2.4 - Solving the Sudoku - solve
def solve():
    digits = [1,2,3,4,5,6,7,8,9]
    for row_idx,row in enumerate(grid):
        for col_idx,column in enumerate(row):
            if column == 0:
                for digit in digits:
                    if possible(row_idx, col_idx, digit):
                        grid[row_idx][col_idx] = digit
                        solve()
                    grid[row_idx][col_idx] = 0
            print_grid(grid)
    return grid

if __name__ == '__main__':
    print_grid(grid)
    print("--")
    print(grid[0][1])
    print(possible(1,0,9))
    print(possible(0,1,5))
    print("++")
    #solve()
