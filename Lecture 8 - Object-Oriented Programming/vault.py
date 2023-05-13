# parent class
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0): # initiating the class
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

# need the str built in function otherwise it will only output what is in memory...with str it will output the vault values
    def __str__(self):
        return f'{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'






# To combine the 2 vaults into 1 in different combinations
# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts

# instead of doing the above...we can use other built in method of classes...Overloaded Operator
# when python sees the + operator it will automatically call in this add function and pass in the 2 operands (left + right)
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts) # calling the class and passing the variables to it...



# Vault 1
potter = Vault(100, 50, 25)
print(potter)

# Vault 2
weasley = Vault(25, 50, 100)
print(weasley)




# Get the total
total = potter + weasley
print(total)