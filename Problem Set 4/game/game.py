import random


while True:  # keeps looping until false
    try:
        level = int(input('Level: '))  # cast string to intenger
        # below we are storing a module(random) in a variable, randint() is the method -- random method takes 2 arguments
        # randint() takes 2 numbers, a start number and a stop number, using these 2 numbers will generate a random number
        game_random_number = random.randint(1, level) # here level replaces the max number
        user_guess = int(input('Guess: '))  # cast string to intenger

        if level <= 0: # Conditionals to reject out of range
            raise ValueError
        if user_guess == game_random_number:  # Conditionals
            print("Just Right!")
            break
        elif user_guess < game_random_number:
            print("Too small!")
        else:
            print("Too Large!")
    except ValueError:
        pass



"""
# OPTION 2 USING FUNCTIONS

def main(): # main function will call on guess_number function that will take user input for guess
    guess_number(level_input())


def level_input(): # level function will run user input for level
    level = 0
    while True: # keeps looping
        try:
            level = int(input("Level: ")) # takes user input as number
            if level <= 0: # conditional for out of range
                raise ValueError
            break
        except ValueError:
            continue
    return level


def guess_number(level): # guess_number function runs the random library and all the conditionals
    number = random.randint(1, level)
    guess = 0
    while guess != number:
        try:
            guess = int(input("Guess: "))
            if guess == number:
                print("Just Right!")
                break
            elif guess < number:
                print("Too small!")
            else:
                print("Too Large!")
        except ValueError:
            continue


if __name__ == "__main__": # protects users from accidentally invoking the script when they didn't intend to
    main()
"""