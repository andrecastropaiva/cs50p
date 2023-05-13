# Take user input
interpreter = input("Interpreter: ")

x, y, z = interpreter.split(" ")

# Convert variables to float
new_x = float(x)
# y represents the operators, so no convertion
new_z = float(z)

# Calculation
if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z
print(result)