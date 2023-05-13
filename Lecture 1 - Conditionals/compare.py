# CONDITIONALS

x = int(input("What's x?"))
y = int(input("What's y?"))

if x < y: # here we are calling a boolean expression (if true print message, if false kepp runing the code to next lines)
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")



# The OR operator
z = int(input("What's z?"))
w = int(input("What's w?"))

if z < w or z > w:
    print("z is not equal to w")
else:
    print("z is equal to w")



# The NOT EQUAL operator
a = int(input("What's a?"))
b = int(input("What's b?"))

if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")



# The EQUAL operator
c = int(input("What's c?"))
d = int(input("What's d?"))

if c == d:
    print("c is not equal to d")
else:
    print("c is equal to d")

