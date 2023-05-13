# Take user input
string = input("Enter the string in camelCase: ")

# target first character in the string, making sure is lowercase and concatenating
string = string[0].lower() + string[1:]

# for loop to iterate over string (i is a name given could be any other name)
for i in string:
#conditional - checks if character is uppercase - if true converts to lower
    if i.isupper():
        string = string.replace(i, f"_{i.lower()}") # this line will convert i if upper case with underscore and lowercase...the f"_{} is called astring and is the same as writing .replace(i, "_" + string(i.lower()) aka concatenating

print(string)