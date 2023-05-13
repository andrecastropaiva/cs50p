"""
# adding while True to keep prompting the user for input
while True:
    try:
        x = int(input("What's x? "))
    except ValueError: # if not an integer handle the error by showing message below to user
        print("x is not an integer")
    else:
        break # exiting the loop once the user input an integer

print(f"x is {x}") # print the input
"""


"""
# adding a function to a while True loop to keep prompting the user for input
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:  # if not an integer handle the error by showing message below to user
            print("x is not an integer")
        else:
            break  # exiting the loop once the user input an integer
    return x # because we are in a function we have to return the value on the variable
"""


# adding a main function to a function that has a while True loop to keep prompting the user for input

def main():
    x = get_int() # get the result from get_int() function and
    print(f"x is {x}")  # print the input from function below

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x  # because we are in a function we have to return the value on the variable and at same time return breaks the loop
        except ValueError:  # if not an integer handle the error by showing message below to user
            pass # this will ignore by not displaying any message for invalid inputs and just keeps prompting what's x


main() # calling main function back
