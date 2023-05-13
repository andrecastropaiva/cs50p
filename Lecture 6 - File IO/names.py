# LIST

# # list where user input will be stored
# names = []

# # Takes user input and prints hello plus the input
# # no variable to store input if we run the program for the second time
# for _ in range(3):
#     names.append(input("What's your name? "))

# # loop to sort the names alphabetically
# for name in sorted(names):
#     print(f"hello, {name}")



# OPEN

# # Variable to save user input
# name = input("What's your name? ")

# # built-in python function to open, create, save, read files
# # -- w means permissions to write to the file although it will not append
# # -- a means permissions to append
# # -- r means permissions to read only
# file = open("names.txt", "a")
# file.write(f"{name}\n") # write() built in function to write to a file, \n creates a new line
# file.close() # close() built in function to close the file completely and save




# # WITH

# # Doing the same as above but using WITH keyword together with open
# # with allows us to open and automatically close the file without using the close()
# # Variable to save user input
# name = input("What's your name? ")


# # built-in python function to open, create, save, read files
# # -- w means permissions to write to the file although it will not append
# # -- a means permissions to append
# # -- r means permissions to read only

# # with instead of a variable then the function open() then name of the variable at the end of the line
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n") # write() built in function to write to a file, \n creates a new line



# # To just read a file without any extra permissions
# with open("names.txt", "r") as file:
#     lines = file.readlines() # readlines() a builtin function to read whats inside a file, so we are storing to a variable - lines


# # Let's say we want to read those lines but printing and returning them as a list -- we need to iterate
# for line in lines:
#     # prints hello plus the name it will read...as is a loop will do that for all lines
#     # it will print with a gap line between the lines as we used \n plus the print function itself adds a new line as well
#     # to remove that line we can just use .strip() .rstrip() or end="" after line
#     print("hello,", line)



# Although what we did above is not very efficient, we are reading  all the lines, then looping then printing
# a better way of doing it the same as above...
# with open("names.txt", "r") as file:
#     for line in file: # loop iterates through the file and each iteration updates the file
#         print('hello,', line.rstrip())




# Although above was almost perfect we are not sorting the names...
# here is the better way...
# names = []
# # if we want to just read the file we dont need to specify with the r
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip()) # this is appending to the list aka to the computer memory, not to the file

# SORTED with WITH
# # now we can sort it -- since they are already in memory...appended above
# for name in sorted(names):
#     print(f"hello, {name}")


# if we just want to sort the file itself...we dont need the list or the second loop to sort it...
# with open("names.txt") as file:
#     for line in sorted(file): # sorts the data in ascending order or A-Z
#         print("hello,", line.rstrip())

# Exactly the same as above but using sorted() with reversing 
with open("names.txt") as file:
    for line in sorted(file, reverse = True): # sorts the data in descending order or Z-A
        print("hello,", line.rstrip())