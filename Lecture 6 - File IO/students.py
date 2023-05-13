# with open('students.csv') as file: # file is a variable
#     for line in file: # loop through
#         # do this
#         row = line.rstrip().split(',') # rstrip() to remove the white space at the end, then split() the line based on the comma --
#         # ultimately split() will return us a list of the separated values, so we will store it in a variable
#         print(f'{row[0]} is in {row[1]}') # row is a list with 2 values, so we are printing the value in index 0 and index 1



# # exactly the same as above but more pythonic
# with open('students.csv') as file: # file is a variable
#     for line in file: # loop through
#         # do this
#         name, house = line.rstrip().split(',') # rstrip() to remove the white space at the end.. split() the line based on the comma
#         # ultimately split() will return us a list of the separated values, so we will store it in two variables (its more readable)
#         print(f'{name} is in {house}') # rnow we can just write th evariable names instead of using indexing



# what if we want to SORT each student...
# Although this is NOT THE BEST PRACTICE (see the next option below)
# we set an empty list
# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         # instead of print we will append it to the list
#         students.append(f'Hello {name} is in {house}')

# # now that is in memory we will SORT
# for student in sorted(students):
#     print(student)


# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {} # create the empty dictionary which will be INSIDE the students list...and soon will have 2 keys name, house
#         student['name'] = name # linking the key (name) to variable name
#         student['house'] = house # linking the key house to the variable house
#         students.append(student) # now we append since students is a list we can use append

# for student in students:
#     # for dictionaries we cant use indexing so we need []
#     print(f"{student['name']} is in {student['house']}") # since all the info is inside the dict which is inside the students list,
#     # this is the way to access it...pay attention to the quotation marks





# BEST PRACTICE - TO SORT IT BY KEY (NAME) (in this case the name of the student)
# although we need to SORT but to use sorted() we need to use key = to specify the key as now students is a dictionary
# so we will write a function to just return the student name as its the key and then pass the function name to key = inside sorted()
# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {'name': name, 'house': house} # instead of creating an empty dictionary as above...we can link the 'keys': variable
#         students.append(student) # now we append since students is a list we can use append


# # defining a function to just return the student names (which are the keys in the dictionary)
# def get_name(student): # pass in the dictionary
#     return student['name'] # just returning student name

# # key = as student is a dictionary, get_name is the name of the function passed in
# # for dictionaries we cant use indexing so we need []
# for student in sorted(students, key = get_name): # if we want to reverse the order A-Z to Z-A we can still use reverse = True
#     print(f"{student['name']} is in {student['house']}") # since all the info is inside the dict which is inside the students list,
#     # this is the way to access it...pay attention to the quotation marks






# Exactly the same as above but sorting the data by student HOUSE insted of NAME done above
# BEST PRACTICE - TO SORT IT BY KEY HOUSE (in this case the HOUSE of the student)
# although we need to SORT but to use sorted() we need to use key = to specify the key as now students is a dictionary
# so we will write a function to just return the student name as its the key and then pass the function name to key = inside sorted()
# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {'name': name, 'house': house} # instead of creating an empty dictionary as above...we can link the 'keys': variable
#         students.append(student) # now we append since students is a list we can use append


# # defining a function to just return the student house (which are the keys in the dictionary)
# def get_house(student): # pass in the dictionary
#     return student['house'] # just returning student house

# # key = as student is a dictionary, get_house is the name of the function passed in
# # for dictionaries we cant use indexing so we need []
# for student in sorted(students, key = get_house, reverse = True): # use reverse = True to sort descending instead of ascending
#     print(f"{student['name']} is in {student['house']}") # since all the info is inside the dict which is inside the students list,
#     # this is the way to access it...pay attention to the quotation marks






# # ANOTHER OPTION - Using Lambda function within key = inside sorted() this way we dont need a separate function
# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {'name': name, 'house': house} # instead of creating an empty dictionary as above...we can link the 'keys': variable
#         students.append(student) # now we append since students is a list we can use append



# # using a lambda (an anonimous function) in key =... student is a argument, then after : is what we want the function to return
# for student in sorted(students, key = lambda student: student['name'], reverse = True):
#     print(f"{student['name']} is in {student['house']}") # since all the info is inside the dict which is inside the students list,
#     # this is the way to access it...pay attention to the quotation marks






# At this point in the lesson we changed the info of students in the CSV ... so we have to change the code...
# at some point when everything starts to become more and more complex, consider using a library
# import csv

# students = []

# with open('students.csv') as file:
#     reader = csv.reader(file) # reader() is part of csv library and we a passing in the variable file (which contains the csv file)
#     # to read it, and store it to a variable 'reader'

#     # now we need to iterate through the reader which is the same as we were doing before, BUT we iterating over the variable
#     # that has the reader()...we NOT iterating over the file variable
#     for row in reader:
#         students.append({'name': row[0], 'home': row[1]}) # row[0] is accessing key in position 0


# # using a lambda (an anonimous function) in key =... student is a argument, then after : is what we want the function to return
# for student in sorted(students, key = lambda student: student['name']):
#     print(f"{student['name']} is from {student['home']}") # since all the info is inside the dict which is inside the students list,
#     # this is the way to access it...pay attention to the quotation marks





# exactly same as above, but using DictReader()...it's more flexible, returns a dictionary
# import csv

# students = []

# with open('students.csv') as file:
#     reader = csv.DictReader(file) # reader() is part of csv library and we a passing in the variable file (which contains the csv file)
#     # to read it, and store it to a variable 'reader'

#     # now we need to iterate through the reader which is the same as we were doing before, BUT we iterating over the variable
#     # that has the reader()...we NOT iterating over the file variable
#     for row in reader:
#         students.append({'name': row['name'], 'home': row['home']}) # for this line to work we had to give column header names
#         # in the csv file, 'name', 'home'


# # using a lambda (an anonimous function) in key =... student is a argument, then after : is what we want the function to return
# for student in sorted(students, key = lambda student: student['name']):
#     print(f"{student['name']} is from {student['home']}") # since all the info is inside the dict which is inside the students list,
#     # this is the way to access it...pay attention to the quotation marks

# NOTE:
# reader() returns lists
# DictReader() returns one dictionary at a time





# TO WRITE TO CSV FILES
import csv

# takes user input
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_write_to_it.csv", "a") as file: # 'a' means append
    # DictWriter, takes two arguments: the file being written to (the csv which is stored in the variable 'file')
    # and the fieldnames to write.
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # writerow function takes a dictionary as its argument.
    # Quite literally, we are telling the compiler to write a row with two fields called name and home.
    writer.writerow({"name": name, "home": home}) # linking the column names of the dictionary to the input variables