counter = 0  # counts the total price

while True:
    try:
        menu = {  # Dictionary stored in menu variable, keys are strings, values are numbers here
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

    # for loop using values() to extract only the values from the dictionary
    # value below, could be named anything
        for value in menu.values():
            # get user input storing it to a variable
            item = input("Item: ").title()
            # adds up and stores user input to calculate total (variable defined at top starting from 0)
            counter = counter + menu[item]
            #print(f"${menu[item]:.2f}") # prints price of item
            print(f"Total: ${counter:.2f}")  # prints total price
            break
    except KeyError:
        pass
    except EOFError:
        break



