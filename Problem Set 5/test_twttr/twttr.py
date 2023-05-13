def main():
    # Asks user input (string) must be done after the loop
    string = input("Input: ")
    shorten(string)

# function with argument string
def shorten(string):
    new_string = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U']  # defining vowels to remove including capitals
    for letter in string: # for loop to iterate
        if letter in vowels: # conditional if i in vowels means if any of the vowels are in the string
            string = string.replace(i, '') # using replace function to replace vowel with no space so removes it
        else:
            new_string += letter
    # print(string) # prints result to console
    return new_string


# function call back and pass user input stored in string variable (line above)
#shorten(string)

if __name__ == '__main__':
    main()