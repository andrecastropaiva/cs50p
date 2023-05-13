# Ask user for their name - whatever is input here will be stored on the variable name
name = input("What's your name? ").strip().title() #prevents multiple whitespaces and makes sure first name starts with a capital

# another way
# Remove white space from string
name = name.strip() # prevents user from entering multiple spaces

# another way
# Capitalize user's name
name = name.capitalize() # makes sure the name starts with a first letter in capital

# Say hello to user
# One way
print("Hello, ", end="")
print(name)

#another way
print("Hello, " + name)

#another way
print("Hello,", name)

#another way
print("Hello," + ' ' + name)

# Say helo to user with quotation marks within quotation marks
print("Hello, \"Andre\"") #this is called escaping

#another way - this way is called special string
print(f"Hello, {name}")
