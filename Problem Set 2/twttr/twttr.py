# function with argument string
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U']  # defining vowels to remove including capitals
    for i in string: # for loop to iterate
        if i in vowels: # conditional if i in vowels means if any of the vowels are in the string
            string = string.replace(i, '') # using replace function to replace vowel with no space so removes it
    print(string) # prints result to console
    #return string


# Asks user input (string) must be done after the loop
string = input("Input: ")

# function call back and pass user input stored in string variable (line above)
remove_vowels(string)
