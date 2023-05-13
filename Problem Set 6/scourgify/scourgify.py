import sys
import csv


# FUNCTION TO CHECK WHAT ARGUMENTS OUTPUT IN THE COMMAND LINE -- as we pass them in...
def command_line_args_check():
    # CONDITIONS
    # CHECK IF ARGUMENTS ARE LESS or EQUAL TO 1 (meaning 1 argument is the name of th epython file itself)
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    # CHECK IF ARGUMENTS ARE OVER 2, output too many arguments
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    # CHECKS IF IT'S A CSV FILE
            # could also do if '.csv' not in sys.argv[1]
    elif sys.argv[1].endswith('.csv') == False:
        sys.exit('Not a CSV file')



# ENGINE to CALL FUNCTIONS BACK and rutn function to read CSVs
def main():
    # Call function back
    command_line_args_check()

    # NEW EMPTY LIST TO STORE DATA FOR NEW CSV
    new_csv_data_file = []
    try:
        # TO READ FILE (in this case csv)...open file in position 1 and read
        with open(sys.argv[1],'r') as file:
            reader = csv.DictReader(file)

            # LOOPS through the each row of the reader (which holds the csv file data)
            for row in reader:
                # storing the columns name & house into variables to then split...
                name = row['name']
                house = row['house']
                # SPLIT name by the comma and space and assign it to 2 variables (first, last)
                first,last = name.split(', ')
                # ASSIGN the variables to the new columns for the new file and append it to the new list
                # basically reordering the new column names for the new file (first to last, and last to first)
                new_csv_data_file.append({'first': last, 'last': first, 'house': house})


        # TO WRITE TO THE NEW FILE...open file in position 2, using DictWriter(), passing the new columns in order, store it to a variable
        with open(sys.argv[2],'w') as new_file:
            writer = csv.DictWriter(new_file, fieldnames = ['first','last','house'])
            # writes the columns to the file
            writer.writeheader()
            # write the data to the new file
            writer.writerows(new_csv_data_file)


     # CHECK IF CSV FILE EXISTS
    except FileNotFoundError:
        sys.exit('Could not read invalid_file.csv')







if __name__ == '__main__':
    main()