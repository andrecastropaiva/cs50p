# importing  sys module/library
import sys

"""
if len(sys.argv) < 2:
    #print("Too few arguments") # prints if no name is passed after name.py
    sys.exit("Too few arguments") # prints and exits
elif len(sys.argv) > 2:
    #print("Too many arguments") # prints if 2 or more names are entered after name.py
    sys.exit("Too many arguments") # prints and exits
else:
    print("hello, my name is", sys.argv[1]) # when we run the program by doing: python name.py Andre in the terminal, it will print the message with my name (only one name or if put between quotes python will understand whatever is inside quotes as one)... [1] is the index number of the name typed in the terminal
"""

for arg in sys.argv[1:]: # [1:] means start at location one and goes till the end by not specifying anything after : (if [1:3] means start at position one untill position 3... the : is the same as implementing slice in a string)
    print("Hello, my name is", arg) # this will print multiple names typed after python name.py in the terminal