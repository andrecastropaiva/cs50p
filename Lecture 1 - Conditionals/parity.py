# MODULE OPERATORS

# Is this number EVEN or ODD?
#x = int(input("What's x? "))

#if x % 2 == 0: # an even number is a number that can be divided by 2
#    print("Even")
#else:
#    print("Odd")


# Creating own function to find Even or Odd
def main(): # 1st function
    x = int(input("What's x? ")) # storing the input in variable x
    if is_even(x): # condition using our own function passing the x value
        print("Even")
    else:
        print("Odd")

def is_even(n): #2nd function using return value in this case a bool
    if n % 2 == 0:
        return True
    else:
        return False

main()



# Creating own function to find Even or Odd (same as above) but using just one line (BEST WAY)

def main():  # 1st function
    x = int(input("What's x? "))  # storing the input in variable x
    if is_even(x):  # condition using our own function passing the x value
        print("Even")
    else:
        print("Odd")


def is_even(n):  # 2nd function using the logic with a return value in this case a bool
    return n % 2 == 0 # here the == gives us the booleans True or False


main()
