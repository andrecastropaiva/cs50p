def main():
    greeting = input("How would you like to set your greeting? ")
    printing_value = value(greeting) # calling back the function below and passing greeting variable (which has user inputs)
    print(f'${printing_value}') # prints value stored in the variable in line above, which holds the values run by below function


def value(greeting):
# defining new variable to store and covert the answer from user input to lowercase and strip bypasses spaces
    new_greeting = greeting.lower().strip()
# Conditionals to verify inputs
# membership operator if...in...
    if "hello" in new_greeting:
        return 0
    elif "h" in new_greeting[0]: # checking if in the input the first letter is an h
        return 20
    else:
        return 100


# calling back main function
if __name__ == '__main__':
    main()