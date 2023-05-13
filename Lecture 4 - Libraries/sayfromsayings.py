import sys # sys gives us access to the command line of python

from sayings import goodbye # here we are importing the function goodbye we wrote in sayings.py

if len(sys.argv) == 2: # this checks that there are 2 names passed when we write python sayfromsayings.py everyone ...being sayfromsayings.pt the 1st and everyone the 2nd
    goodbye(sys.argv[1]) # here we are running the goodbye function passing as argument the index in 1 which is everyone as an example


# NOTE: Difference between module/library and package is that module/library is run from a file and a package is run from a folder