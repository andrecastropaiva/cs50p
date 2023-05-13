 # LOOPS

# While loop
i = 0
while i < 3:
    print("meow")
    i += 1 # this is a better way of doing i = i + 1 (python doesn't allow i++)




# While True loop
while True: # good option when we want to get user input to match our expectations
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n): # _ is just a random symbol/word, could be anything else
    print("meow")





# For loop (allows us to iterate through a LIST(array) of items)
for i in [0, 1, 2]: # first iteration i = 0 then prints "meow"...second iteration i = 1 then prints meow...third iteration i = 2 then prints meow and stops
    print("meow")


# using a for loop with a range() function so we can specify exactly how many times we want to iterate
for i in range(3):
    print("meow")



# NOTE: can also use multiplication (NOT GOOD PRACTICE)
print("meow\n" * 3, end="")





# PUTTING THE SAME LOGIC INTO A FUNCTION
def main(): # defining main function
    meow(3) #calling a new function inside the main function and passing 3 as value

def meow(n): #defining the function called above
    for _ in range(n): #looping using range function that takes n as argument (which is 3 as it was passed above) (basically we are chaining all the functions)
        print("meow")

main() # calling the main function which will run all the chains of other functions


# PUTTING THE SAME LOGIC INTO A FUNCTION BUT CREATING OUR OWN FUNCTION NAME
def main():  # defining main function
    number = get_number() # creating function and calling it get_number, storing the values in number variable
    meow(number)  # calling a new function inside the main function and passing whatever value is stored in number variable (which will be whatever user inputs when prompted)


def get_number(): # defining the function called above
    while True: #using while loop to iterate
        n = int(input("What's n? ")) #setting input to intenger
        if n > 0: #condition
            break
    return n #return the value passed on in the input by the user


def meow(n):  # defining the function called above
    for _ in range(n):  # looping using range function that takes n as argument (which is 3 as it was passed above) (basically we are chaining all the functions)
        print("meow")


main()  # calling the main function which will run all the chains of other functions
