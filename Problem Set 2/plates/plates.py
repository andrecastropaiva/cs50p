def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(i): # i represents the string
    # first condition max 6 characters (6 bigger or equal than input length) and min 2 characters
    # second condition i[0:2].isalpha() means ensuring characters at position 0 and 1 (as the last isnt inclusive, to reach 1 we have to put 2) index are letters
    # third condition i.isalnum() means that after the letters only contains numbers
    if 6 >= len(i) >= 2 and i[0:2].isalpha() and i.isalnum():
        for characters in i: # for loop to iterate through characters
            if characters.isdigit():
                string_index = i.index(characters) # index could be named anything and will store the result of iteration
                if i[string_index:].isdigit() and int(characters) != 0:  # check if the end of string are digits and the first digit used isnt zero
                    return True
                else:
                    return False
        return True # if above conditions are True, return Valid
    else:
        return False # if not True, return False



main()
