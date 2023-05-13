while True:

    try:
        # Below split with a slash means the input when sees a slash with split 1 sentence in 2... so if input is 1/2 as one, the split allows 1 input to be split in 2 assigning each of them to each variable...Note the [] so they input will be in a list as 2 separate indexes
        x, y = [int(x) for x in input("Fraction: ").split('/')]

        percentage = round(int(x * 100) / y)  # calculating the input numbers

        if percentage >= 99 and percentage <= 100:
            print("F")
            break
        elif percentage <= 1:
            print("E")
            break
        elif percentage > 1 and percentage < 99:
            print(f"{percentage}%")
            break
        elif percentage == 0:
            print("Invalid input")
            break
    except (ValueError, ZeroDivisionError):
        pass



