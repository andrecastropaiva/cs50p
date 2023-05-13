for _ in range(3):
    print("#")



# FUNCTION (does the same as the above but with our own function) (vertical)
def main():
    print_column(3)



def print_column(height):
    for _ in range(height):
        print("#")


main()




# FUNCTION 2 (horizontal)
def main():
    print_row(4)


def print_row(width):
        print("?" * width)


main()







# FUNCTION 3 - same as both functions above (square)
def main():
    print_square(3)


def print_square(size):
    # for each row in square
    for i in range(size):
        print("#" * size) # string multiplication trick

main()