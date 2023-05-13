import cowsay # imports the cowsay package
import sys

"""
if len(sys.argv) == 2: # this means if the user provided just 2 names, name of the file and their name for example then will run the line below
    cowsay.cow("hello, " + sys.argv[1]) # this will print the string plus the name entered which will be in index 1 hence why number 1...index 0 is the name of the file say.py in the code with a cow as a graphic
"""


if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1]) # .trex will print a dinnosaure instead of a cow
