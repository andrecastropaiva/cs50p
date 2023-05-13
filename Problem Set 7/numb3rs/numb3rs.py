import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression to match IPv4 address pattern
    # each sets between each parentheses are considered a group
    pattern = re.search(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$', ip)

    # checks if pattern is not None and all non-empty capturing groups in pattern match integers between 0 and 255 (inclusive)
    # using a generator expression and the built-in all() function
    return pattern is not None and all(0 <= int(group) <= 255 for group in pattern.groups() if group)



# OPTION 2
'''
    if pattern:
        for group in pattern.groups():
            if int(group) > 255:
                return False
        return True
    else:
        return False
'''


# check if the current module is being executed as the main program or if it is being imported as a module by another script
if __name__ == "__main__":
    main()