def main():
    greeting = input("How would you like to set your greeting?")

# defining new variable to store and covert the answer from user input to lowercase and strip bypasses spaces
    new_greeting = greeting.lower().strip()
# Conditionals to verify inputs
# membership operator if...in...
    if "hello" in new_greeting:
        print("$0")
    elif "h" in new_greeting[0]: # checking if in the input the first letter is an h
        print("$20")
    elif new_greeting == "how you doing?":
        print("$20")
    elif new_greeting == "what's happening?":
        print("$100")
    elif new_greeting == "what's up?":
        print("$100")
    else:
        print("Invalid input")



# calling back main function
main()