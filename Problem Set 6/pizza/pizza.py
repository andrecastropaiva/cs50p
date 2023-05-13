import sys
import csv
from tabulate import tabulate


# CHECK HOW MANY ARGUMENTS WE HAVE IN THE COMMAND LINE
# sys.argv return a list with arguments passed in the command line (whichever we pass in even if they dont exist)
def command_line_args_check():
        # CHECKS MIN LENGTH...if less or equal to 1 file, displays the message below
        if len(sys.argv) <= 1:
            sys.exit('Too few command-line arguments')
            # CHECKS MAX LENGTH...if over 2 files shows the messages below
        elif len(sys.argv) > 2:
            sys.exit('Too many command-line arguments')
            # CHECKS IF IT'S A CSV FILE
            # could also do if '.csv' not in sys.argv[1]
        elif sys.argv[1].endswith('.csv') == False:
            sys.exit('Not a CSV file')




# ENGINE to run function to read csv and call back functions
def main():
    # CALL BACK FUNCTIONS
    command_line_args_check()

    # READ CSVs
    try:
        # OPENS FILE IN INDEX 1 (which is the CSV) -- file is a variable
        with open(sys.argv[1], 'r') as file:
            # DictReader to return a dictionary, passing the file variable where the csv file is stored
            reader = csv.DictReader(file) # could also use reader() (which returns lists per each line) instead of DictReader()
            # which returns dictionaries per each line
            # headers = 'keys' refers to the columns which in the dict are the keys ...tablefmt is just the shape of the table
            print(tabulate(reader, headers = 'keys', tablefmt="grid"))
    # CHECKS IF FILE EXISTS
    except FileNotFoundError:
        sys.exit('File does not exist')





if __name__ == '__main__':
    main()



# NOTE:
# OPTION 2:
# withing try: I could also use the following...

# with open(sys.argv[1], 'r') as file: # file can be called anything (it's a variable)
    # setting an empty list to append the lists generated from reader()
    # table = []
    # reader() returns lists per each line in the csv --- built-in function from csv library
    # reader = csv.reader(file)
    # LOOPS through reader where csv is stored and per each row appends to the table list...so we will have a list containing lists
    # for row in reader:
        # table.append(row)
# table[1:] means passing on the variable table from row 1 onwards, as row 0 is the columns which are in the headers
# headers = table[0] refers to the columns which are in the first list as they are in the first row of csv
# ...tablefmt is just the shape of the table, is part of the library tabulate
# print(tabulate(table[1:], headers = table[0], tablefmt="grid"))