from datetime import date
import re, sys
import inflect

# initialize an inflect engine to convert numbers to words
p = inflect.engine()

# define the main function that gets the user's birth date, validates it,
# calculates the difference between the birth date and today's date in minutes, and displays the result in words
def main():
    # get the user's birth date as a string input
    birthdate_input = input("Date of Birth: ")
    # try to validate the input date using the check_bdate function
    try:
        year, month, day = check_bdate(birthdate_input)
    # if the date is invalid, exit the program with an error message
    except:
        sys.exit("Invalid Date")

    # create a date object from the validated year, month, and day
    date_of_birth = date(int(year), int(month), int(day))

    # calculate the difference between the birth date and today's date in minutes
    difference = date.today() - date_of_birth # returns a timedelta object with number of days difference
    minutes = difference.days * 24 * 60 # to get the minutes I get the days * 24 (number of hours/day) * 60 number of minutes/hour

    # convert the difference in minutes to words using the inflect engine
    date_to_words = f"{p.number_to_words(minutes, andword='').capitalize()} minutes"

    # display the difference in minutes as words
    print(date_to_words)




# define the check_bdate function that checks if a string input matches the
# format "YYYY-MM-DD" using a regular expression
def check_bdate(birth_date):
    pattern = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date)
    # if the input matches the pattern, split it into year, month, and day
    if pattern:
        year, month, day = birth_date.split("-")
        return year, month, day




# call the main function if the script is run as the main program
if __name__ == "__main__":
    main()