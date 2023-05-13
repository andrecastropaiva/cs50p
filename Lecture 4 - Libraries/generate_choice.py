# Libraries or modules are the same in Python
# importing it like this: import random - imports the whole module which sometimes can be very big
#import random
# like the line below Python will be a lil smarter and import just the choice function (nothin else)
from random import choice

# I wanted to store it in a variable
# the choice function below divides the probability of the number of arguments (2 arguments, 50% probability to each, 3 arguments 33% probability to each and so on)
# coin = random.choice(["heads", "tails"]) # this is taken from the python library docs (choice function that takes sequence as argument which is essentially a list)
coin = choice(["heads", "tails"]) # dont need to call random because above i just imported choice
print(coin)



