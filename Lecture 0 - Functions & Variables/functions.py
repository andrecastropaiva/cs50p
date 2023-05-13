# FUNCTIONS
def hello(to="world"): # def is short for define , chose to call the parameter to, then can assign a value to the parameter
    print("Hello,", to)

hello() # calling the function without parameters
name = input ("What's your name? ")
hello(name) # here the function hello() is being used to pass the argument/parameter name


# organising the code when using 2 functions - example
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("Hello,", to)


main() # here thats where the magic happens, calling main has the ability to run the main function as well as the hello function



