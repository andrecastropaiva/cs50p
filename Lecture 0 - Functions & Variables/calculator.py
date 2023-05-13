# INTEGERS

# one way
x = int(input("What's x?"))
y = int(input("What's y?"))

print(x + y)


# another way
x = input("What's x?")
y = input("What's y?")

z = int(x) + int(y)
print(z)


# another way (NOT GOOD PRACTICE)
print(int(input("What's x?")) + int(input("What's y?")))




# FLOAT
x = float(input("What's x?"))
y = float(input("What's y?"))

print(x + y)




# another way - round to the next integer
x = float(input("What's x?"))
y = float(input("What's y?"))

z = round(x + y)

print(z)



# another way - adding commas on the numbers
x = float(input("What's x?"))
y = float(input("What's y?"))

z = round(x + y)

print(f"{z:,}") # adding commas to long numbers (colon followed by comma)




# Division
x = float(input("What's x?"))
y = float(input("What's y?"))

z = round(x / y, 2) # round to the nearest number by adding comma 2 (not integer...for example 0.6666666 would round to  0.67)

print(z)




# another way
x = float(input("What's x?"))
y = float(input("What's y?"))

z = x + y

print(f"{z:.2f}") # this is specifying how many digits I want to print , for example if x is 2 and y is 3, dividing would return 0.67




# RETURNING A VALUE WITH A FUNCTION
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x)) # gere square will return the square of a value when we run the function below


def square(n):
    return n * n


main()
