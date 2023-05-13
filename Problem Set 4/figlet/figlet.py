import sys
from pyfiglet import Figlet
import random


figlet = Figlet() # initiating figlet
fonts = figlet.getFonts() # storing the fonts to a variable

generate = random.choice(fonts) # using random to randomly pick the fonts and store to a variable

# CONDITIONALS
if len(sys.argv) < 2:
    fig = Figlet(font = generate)
    user_input = input("Input: ")
    print(fig.renderText(user_input))
elif (sys.argv[1]) == ("-f") and sys.argv[2] in fonts or (sys.argv[1]) == ("--font") and sys.argv[2] in fonts:
    fig = Figlet(font = sys.argv[2])
    user_input = input("Input: ")
    print(fig.renderText(user_input))
else:
    sys.exit("Invalid input")


