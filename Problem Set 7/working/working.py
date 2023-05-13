import re




# Define the main function that prompts for input and calls the convert function
def main():
    print(convert(input("Hours: ")))




# Define the convert function that converts a string input containing two times separated by "to" into a formatted string
def convert(s):
    # Define the regular expression pattern to match the input format
    pattern = re.search(r"^([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M) to ([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M)$", s)
    # Check if the pattern matches the input string
    if pattern:
        # If the pattern matches, extract the matched groups...groups() returns a tuple
        matched = pattern.groups()
        # Convert the two times to the 24hr format and return the formatted string
        return f"{convert_time(matched[:3])} to {convert_time(matched[3:])}"
    # If the pattern does not match, raise a ValueError
    raise ValueError




# Define the convert_time function that converts a single time in the format (hh, mm, AM/PM) to the desired format (hh:mm AM/PM)
def convert_time(time):
    # If the hour is "12", convert it to "00" or "12" based on the AM/PM indicator
    if time[0] == "12":
        hours = "00" if time[2] == "AM" else "12"
    # If the hour is not "12", add 12 to it if the AM/PM indicator is PM
    else:
        hours = f"{int(time[0]):02}" if time[2] == "AM" else f"{int(time[0]) + 12}"
    # If the minutes are None, set them to "00", otherwise format them with leading zeros
    # time[1] is the AM or PM...if none add 00... :02 is 2 numericals e.g. 00:00 instead of 0:00
    minutes = "00" if time[1] is None else f"{int(time[1]):02}"
    # Return the formatted time string
    return f"{hours}:{minutes}"




# Call the main function if this script is run as the main program
if __name__ == "__main__":
    main()