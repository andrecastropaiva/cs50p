# Implements sort() with a class method

import random

# here is the same as what I did in the other file but without self and without instantiating the class
class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class variable of type list

# a class method just means we can call this method without instantiating a 'Student' object first
    @classmethod # decorator
    # class method
    def sort(cls, name): # cls means class which allows me to access the method (basically replaces self)
        print(name, "is in", random.choice(cls.houses))

# no instantiation...just calling the class with the method
Hat.sort("Harry")
