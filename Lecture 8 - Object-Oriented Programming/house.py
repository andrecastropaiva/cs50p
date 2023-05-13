name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # case do thi with a separation | (meaning OR) because makes sense as the print is the same for the 3 names
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who!")
