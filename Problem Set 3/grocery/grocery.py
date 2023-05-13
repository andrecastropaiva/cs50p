grocery = {}  # empty dictionary outside loop

while True:  # keeps running until false (so keeps asking user input)
    try:
        # take user input store in variable, split in 2 pairs...key and value
        item = input(" ")
        # grocery[item] accesses the dictionary items...then, using get() to get the item input from user and provides a default value of Zero if input not in the dictionary, if it is, keep adding one for each time the same item is input
        grocery[item] = grocery.get(item, 0) + 1

    except EOFError:
        # loop to output key (which is the name of items) and value (which is the number) of the item and sort them alphabetically
        for key, value in sorted(grocery.items()):
            # print them in uppercase, value being first
            print(value, key.upper())
        break




"""
# SECOND WAY TO SOLVE THIS WITH IF ELSE STATEMENT
grocery = {}

while True:
    try:
        user_input = input("").split("\n") # split input as soon as it encounters a space --- if there's no space (i.e. only one item is entered this time, this gives a list with a single item in it. (the word entered)
        for item in user_input:
            if item in grocery.keys():  # if the item exists, add 1 to its counter
                grocery[item] += 1
            else:  # if the item doesn't exist, set its counter to 1
                grocery[item] = 1

    except EOFError:
        for key, value in sorted(grocery.items()): # for loop to go through keys and values and sort all the items in the dictionary alphabetically and in capital letters
            print(value, key.upper())
        break
"""



"""
# THIRD WAY TO SORT THIS (ALTHOUGH COULDN"T GET GREEN CHECKS, IT WORKS AS EXPECTED)
import sys

grocery = {}

while True:
    try:
        user_input = input("")
        user_input = sys.stdin.read().split("\n")
    # if there's no space (i.e. only one item is entered this time, this gives a list with a single item in it. (the word entered)
        for item in user_input:
            if item in grocery.keys():  # if the item exists, add 1 to its counter
                grocery[item] += 1
            else:  # if the item doesn't exist, set its counter to 1
                grocery[item] = 1

    except EOFError:
        for key, value in sorted(grocery.items()):
            print(value, key.upper())
        break
"""