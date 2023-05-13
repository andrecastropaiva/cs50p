# LISTS aka (arrays)
students = ["Hermione", "Harry", "Ron"]
print(students)

print(students[0]) # print item at location 0...aka "Hermione"

# Another way is to use for loop
for student in students: # printing all the students one in each line
    print(student)


# Another way is using length (can't use range() on its own as it expects a integer and the list has names not numbers)
for i in range(len(students)):
    print(i, students[i]) # print can take 2 parameters





# DICTIONARIES
students2 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }

print(students2)
print(students2["Hermione"]) # prints the value of "Hermione" which is "Gryffindor"
print(students2["Draco"]) # prints the value of "Draco" which is "Slytherin"



# Another way is using a for loop
for student2 in students2:
    print(student2, students2[student2], sep=", ") # prints the keys and values, the sep=", " adds a comma and a space between keys and values





# Another DICTIONARY with more info
students3 = [ # List (array) - a collection of key value pairs
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, # dictionary 1
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, # dictionary 2
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"}, # dictionary 3
    {"name": "Draco", "house": "Slytherin", "patronus": None} # dictionary 4
]

# With the option above we can still use a for loop to iterate
for student3 in students3:
    print(student3["name"], student3["house"], student3["patronus"], sep=", ")