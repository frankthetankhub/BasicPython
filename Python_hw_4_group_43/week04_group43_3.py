#Task 4.3 - Bottle Return Machine
# import necessary method from package random
from random import randint
# create the variables to be printed later and inp for while condition
bottles = []
total_price = 0.0
inp = ""
# continue to ask for bottles until "finish" is entered
while inp != "finish":
    # create dictionary for each bottle
    bottle = {"name": "","price": 0.0, "ID": 0}
    inp = input("Please enter the next bottle's name: \n")
    # if "finish" is entered print all bottles
    if inp == "finish":
        print(bottles)
        # calculate total price
        for bottle in bottles:
            total_price += bottle["price"]
        # and print the total price in the correct format
        print(f"The total price is {format(total_price, '.2f')}.")
    else:
        # if a bottle name is entered ask for the price for the bottle and convert to float for calculation of total price later
        price = float(input(f"Thank you. Please enter the price of {inp}:\n"))
        # update our bottle dictionary
        bottle["name"] = inp
        bottle["price"] = price
        # create random ID as string to append numbers
        ID = ""
        for i in range(3):
            ID += str(randint(0,9))
        # and save ID as an integer in the dictionary
        bottle["ID"] = int(ID)
        # add the whole bottle entry to the list of total bottles
        bottles.append(bottle)
