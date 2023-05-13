# Inheritance example...

# 3rd class done after the other 2...basically to combine the functionality of the other 2 classes into 1
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name')
        self.name = name # since name is on both of those classes, we can inherit from them


class Student(Wizard): # inherit from Wizard class
    def __init__(self, name, house):
        super().__init__(name) # this is a reference to the super class (parent class), (in this case Wizard class) of this child class
        # passing to init what we want to inherit
        self.house = house # this object is unique to student, so has to be here only



class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) # this is a reference to the super class (parent class), (in this case Wizard class) of this child class
        # passing to init what we want to inherit
        self.subject = subject # this object is unique to professor, so has to be here only




# Instantiating the classes and methods
wizard = Wizard('Albus')
student = Student('Harry', 'Gryffindor')
professor = Professor('Severus', 'Defense Against the Dark Arts')