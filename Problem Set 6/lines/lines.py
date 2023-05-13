import sys # has many functions and variables that are useful to manipulate python runtime environment (command-line arguments)


# CHECK HOW MANY ARGUMENTS WE HAVE IN THE COMMAND LINE
def command_line_args_check():
    # CONDITIONS TO CHECK HOW MANY ARGUMENTS WE HAVE IN THE COMMAND LINE (in the directory we working in)
    if len(sys.argv) <= 1:
        #print(sys.argv) # prints the file names in this directory (returns a list)
        sys.exit('Too few command-line arguments') # quits the program and displays this message
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    # CHECK IF IT IS A PYTHON FILE
    # argv[1] is the first element to check (argv[0] is the python file itself...), if endswith('.py') equals False meaning no '.py'
    # in that position
    elif sys.argv[1].endswith('.py') == False:
        sys.exit('Not a Python file')


# TO CHECK WHICH LINES WE COUNT
def line_check(line):
    if line.isspace(): # checks if it is whitespace (empty line)
        return True # if returns True means it is a whitespace
    elif line.strip().startswith("#"): # checks if the line has spaces at the beginning and at the end & if it starts with # (aka comment)
        return True # if returns True means it has spaces at the beginning or end & is a comment we are not gonna count
    return False # else we will count





# ENGINE to read the file and call all functions back
def main():
    # calling function back
    command_line_args_check()

    # OPEN FILES
    try:
        with open(sys.argv[1], 'r') as file: # to open the file ...file is a variable
             # to read the file
            lines = file.readlines()
            # print(lines)
    except FileNotFoundError: # raising exception if file doesnt exist
        sys.exit('File does not exist')



    # set counter to store the number of lines
    line_counter = 0
    # loops through the lines
    for line in lines:
        # condition...the function above passed in
        if line_check(line) == False: # if False means not a comment, not a whitespace, so we will count
            line_counter += 1 # add 1 to the counter variable per each valid count iteration
    print(line_counter)




if __name__ == '__main__':
    main()