# This is a list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# keeps looping until false
while True:
    try:
        date = input("Date: ")  # prompts user for their input
        month, day, year = date.split("/") # spliting by forward slash user input which is stored in date variable in 3 variables month, day, year
        # conditional to check if month is between 1 and 12 and day between 1 and 31
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try: # this part of the code will convert the former date format into a new format
            former_month, former_day, year = date.split(" ") # splitting the former format of date by space... and soting in new variables
            # here we are finding the  number of the month from the list above
            for index in range(len(months)): # loop through a range to loop up to the length of the list of months
                if former_month == months[index]: # conditional to check if former month matches each month index position in the list
                    month = index + 1 # because indexes start at position 0 we are saying that month is 0 + 1, so from here the index starts at 1

            day = former_day.replace(",", "") # here as the former day had a come next to the day we are removing the comma for a space

            # conditional to check if month is in between 1 and 12 and day between 1 and 31
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

# formatting the result... if day or month are between 1 and 9 add a 0 before... so becomes 01, 02, 03 etc..
print(f"{year}-{int(month):02}-{int(day):02}")




