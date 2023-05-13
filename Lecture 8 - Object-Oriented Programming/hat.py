# Implements sort() with an instance method

# library
import random


class Hat:
    def __init__(self): # initiation
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# defining the method
    def sort(self, name):
        print(name, "is in", random.choice(self.houses)) # using random library with method choice to shuffle the list of houses

# Instantiation
hat = Hat()
hat.sort("Harry") # calling method attached to thhe variable hat, which contains Hat() class




