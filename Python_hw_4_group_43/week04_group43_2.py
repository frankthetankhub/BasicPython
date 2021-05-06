# Task 4.2 - Creating Data Structures
## Task 4.2.1 - Choosing Data Structures
### 1.
musicians = ["Helene Fischer", "Dieter Bohlen", "Hans Entertainment"]   # list since 3 unrelated entries which are changable
### 2.
colors = ["Black", "Green"]                                             # list since 2 unrelated entries which can change
### 3.
lectures = {"Kreative Erotikromane schreiben für Anfänger" : "J.K. Rolling",
            "How to avoid your angry mom for more than a week?" : "Bart Simpson",
            "How to knockout a Camel?" : "Arnold Schwarzenegger"}       # dictionary since every lecture (key) has a lecturer (value) associated with only that lecture so we have key-value pairs
### 4.
months = {"January", "February", "March", "April", "May"}               # set since the values don't change and the order is not important for the question to simply name the first 5
### 5.
John_Wick = ("Don't kill my Dawg Avenue", 33, "New York")               # tuple since the adress is one complete data and doesn't change regularly

## Task 4.2.2 - Indexing Errors
my_list = [2, 3, 9, 1]
# print(my_list["1"])            #TypeError: the indexing can't be a string like "1" is it should be an integer like 1
my_list[1] = 9
my_list[0] = my_list[1]
print(my_list[:2])

# for number in my_list:
#     print(my_list[number])    #IndexError: since number takes the values of the elements in my_list it can't be used this way, in the first
                              # iteration of the for loop number will already be 9 which is out of range as an index for my_list, print(number)
                              # would lead to the desired output

my_tuple = ("banana", "apple", "cucumber")
print(my_tuple[-1])
# my_tuple[1] = "green_apple"     #TypeError: the values in a tuple can't be changed, the way they are changed here would work if my_tuple was a
                                # list but not for a tuple

# my_set = {my_tuple[0], my_list[-1]) #SyntaxError: the { can't be finished with a different bracket ), the ) should be a }
# print(my_set[0])                    #NameError: since my_set is not implemented correctly it is not defined yet,
                                    #otherwise: TypeError: Even if my_set was defined at this point the line would result in a TypeError since sets are not subscriptable

my_dict = {"tuple": my_tuple, "list": my_list}
print(my_dict["tuple"])

## Task 4.2.3 - Iteratively Creating Lists
### import necessary method from package random
from random import randint

def make_random_grid(entries, size):
    """returns a grid of type list with shape[entries][size]

        entries: integer giving the number of entries in the grid
        size:    integer giving the length of each entry
    """
    ### implement the grid which will be returned later
    grid = []
    for i in range(entries):
        ### set column to empty list for every new entry
        column = []
        ### create each entry with "size" number of random integers between 0-99
        for j in range(size):
            column.append(randint(0,99))
        ### append each entry to our grid
        grid.append(column)
    return grid

print(make_random_grid(3,4))
