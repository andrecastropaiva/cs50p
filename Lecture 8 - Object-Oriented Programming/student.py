
# INTRO TO CLASSES & PROPERTIES (MOVED TO THE TOP)
class Student:  # Student capital S is an object of the class
    def __init__(self, name, house, patronus): # init is a method (a function inside class) that has priority in python classes
        if not name: # this is the same as if name == ""
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name # self.name is like a variable and allows us to initialise in an empty object name and house
        self.house = house # here is deliberately not _house to make the code run through the functions Getter and Setter which already have the error checks
        self.patronus = patronus


    def __str__(self): # str is a method from classes in python
        return f"{self.name} from {self.house}"


# def house part of PROPERTIES
# Getter function
    @property # decorator
    def house(self):
        return self._house # the underscore means for not touching, gives some priority
# Setter function - it will be called anytime I try to access .house
    @house.setter # decorator ...a clue to python that helps python easily understand when I want to access to house function...
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


    # create own function inside class
    def charm(self):
        if self.patronus == "Stag":
            return "🦌"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russell Terrier":
            return "🐕"
        else:
            return "🏁"



def main():  # using get() to get name and house
    student = get_student()
    student.house = "Number Four, Privet House" # can't be executed as the house function (setter) above sees we trying to access .house
    # with different values (not current ones)
    print("Expecto Patronum!")
    print(student.charm()) # calling back the charm function created above
    #print(f"{student.name} from {student.house}")

def get_student():
    #student = Student()  # creating student object
    #student.name = input("Name: ")
    #student.house = input("House: ")
    #return student
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) # student with capital S is a function, passing two arguments name and house, this function constructs an object


if __name__ == "__main__":
    main()



"""
# OPTION 1
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
"""


"""
# OPTION 2 using functions (a list)
def main(): # using get() to get name and house
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name(): # sets input for name
    return input("Name: ")


def get_house(): # sets input for house
    return input("House: ")


main() # calling back main which in turn calls back the other 2 functions as well
"""

"""
# OPTION 3 : using a tuple
def main():  # using get() to get name and house
    student = get_student()
    if student[0] == "Padma":
        student[1] == "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():  # using get() to get name and house
    name = input("Name: ")
    house = input("House: ")
    return (name, house) # this is called a tuple with 2 values


if __name__ == "__main__":
    main()
"""

"""
# OPTION 4 - using a dictionary
def main():  # using get() to get name and house
    student = get_student()
    if student["name"] == "Padma": # the way to index through dictionaries is with the varibales instead of the numbers
        student["house"] == "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():  # using get() to get name and house
    student = {} # sets the dictionary
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
"""



