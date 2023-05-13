import sys
import requests


def main():
    print(f"${bitcoin_rate() * user_input(sys.argv):,.4f}")  # this 3 functions will calculate the rate we are getting from API times the user input and converts to USD format with :,.4f

# This function handles user input an runs through conditionals

try:
    def user_input(argv):
        user_input = 0  # this will count the user input
        if len(argv) == 1:  # when runnin code if there is only one argument aka file name
            sys.exit("Missing command-line argument")
        elif len(argv) > 2:  # if there is more than 2 arguments aka filename plus number of bitcoins plus something else
            sys.exit("Invalid input")
        else:
            # if correct aka argument at positon 0 (file) and argument at position 1 (number of bitcoins) (allows the user input to be in float format)
            user_input = float(argv[1])
            return user_input
except ValueError:  # if argument passed isn't a number
    sys.exit("Command-line argument is not a number")


# this function handles the API
try:
    def bitcoin_rate():
        bitcoin_rate = 0
        # API URL stored in a variable
        request = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        response_api = request.json()  # request in json and stores the response_api in a variable
        # in the line below is what we want to extract from the API...value of bitcoin in USD and in float format...basically thats the name of the folders...inside bpi folder is USD and inside USD there are different formats...in this case we want rate float
        bitcoin_rate = response_api["bpi"]["USD"]["rate_float"]
        return bitcoin_rate
except requests.RequestException:  # handles the error
    sys.exit("Error requesting. Try again!")



if __name__ == "__main__":
    main()
