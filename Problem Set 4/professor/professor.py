import random


def main():
    user_level = get_level()
    print(calculate(user_level))


def get_level():
    level = 0 # will store the level chosen by the user
    while True:
        try:
            level = int(input("Level: ")) # take user input for level
            if 0 >= level or level > 3: # conditional to make sure user chooses between 1 and 3 otherwise keeps asking
                raise ValueError
            break
        except ValueError:
            continue
    return level


def generate_integer(level):
    base = level - 1
    start = [0, 10, 100] # level 1 from 0 -- level 2 from 10 -- level 3 from 100
    stop = [9, 99, 999] # level1 to 9 -- level 2 to 99 -- level 3 to 999
    return random.randint(start[base], stop[base]) # numbers will be randomly generated and the variables above will limit depending on the level chosen


def calculate(level):
    score = 10

    for _ in range(10): # for loop using range as method and passing 10 as argument (the underscore means the value isnt important and loop will only run for 10 times)
        num1 = generate_integer(level) # one number stored in num1
        num2 = generate_integer(level) # second number stored in num2
        sum = num1 + num2 # sums up
        first_try = True
        incorrect = 3 # this sets the number of errors before showing the correct answer

        while True: # keeps looping
            try:
                answer = int(input(f"{num1} + {num2} = ")) # this will store the answer from user
                break
            except ValueError: # All conditionals to handle wrong answers till the end
                if first_try:
                    score -= 1
                    first_try = False
                incorrect -= 1
                if incorrect == 0:
                    print(sum)
                    break
                print("EEE")
                continue
        if answer != sum:
            if first_try:
                score -= 1

            while answer != sum: # another loop to handle wrong answers
                try:
                    incorrect -= 1 # conditionals for wrong answers
                    if incorrect == 0:
                        break
                    print("EEE")
                    answer = int(input(f"{num1} + {num2} = "))
                except ValueError:
                    incorrect -= 1
                    print("EEE")
                    continue
            print(sum)

    return f"Score: {score}"


if __name__ == "__main__":
    main()
