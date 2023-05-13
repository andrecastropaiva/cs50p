def main():
    # defining fraction to be input
    fraction = input('Fraction: ')
    # store result of the convert(fraction) in variable
    converted_fraction = convert(fraction)
    # passing the convert(fraction) result stored in converted_fraction to gauge(percentage) and store in variable
    result = gauge(converted_fraction)
    print(result) # print result


# this function will CALCULATE PERCENTAGE
def convert(fraction):
    while True: # continues to loop while True
        try:
            # split input from string to fraction (splitting into 2 values)
            numerator, denominator = fraction.split('/')

            # convert numerator & denominator (th e2 values from input()) to integers
            numerator = int(numerator)
            denominator = int(denominator)

            # calculate percentage
            fraction_calculation = numerator / denominator  # calculating the input numbers (already ints)
            # adding condition
            if fraction_calculation <= 1:
                # multiply percentage by 100 if lower or equal than 1
                percentage_times_100 = int(fraction_calculation * 100)
                return percentage_times_100
            else:
                return fraction
        # if numerator higher than denominator, raises valueError
        # if divided by zero raises ZeroDivisionError
        except (ValueError, ZeroDivisionError):
            raise


# it will return the RESULTS based on condition checks
# takes an integer, returns a string
def gauge(percentage):
    # convert string to integer to perform comparisons
    percentage = int(percentage)
    # conditions
    if percentage >= 99 and percentage <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"



if __name__ == '__main__':
    main()
