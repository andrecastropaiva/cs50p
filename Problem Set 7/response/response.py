# this library already has the regex pre-built in the is_email() method
from validator_collection import checkers

# here we just need to use the method is_email to check the input
def main():
    print('Valid') if checkers.is_email(input("What's your email address? ")) == True else print("Invalid") # if email validates true
    # print valid else invalid



# check if the current module is being executed as the main program or if it is being imported as a module by another script
if __name__ == "__main__":
    main()