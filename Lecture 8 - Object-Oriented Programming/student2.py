class Student:  # Student capital S is an object of the class
    def __init__(self, name, house): # init is a method (a function inside class) that has priority in python classes

        self.name = name # self.name is like a variable and allows us to initialise in an empty object name and house
        self.house = house # here is deliberately not _house to make the code run through the functions Getter and Setter which already have the error checks



    def __str__(self): # str is a method from classes in python
        return f"{self.name} from {self.house}"


# a class method just means we can call this method without instantiating a 'Student' object first
    @classmethod # decorator
    # class method
    def get(cls): # cls means class which allows me to access the method (basically replaces self)...can be called anything but by
        # convention is better practice naming it cls
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # using the classmethod to pass the variables, I can now instantiate by using cls





def main():  # using get() to get name and house
    student = Student.get() # here I'm instantiating the class Student by calling the method
    print(student)




if __name__ == "__main__":
    main()