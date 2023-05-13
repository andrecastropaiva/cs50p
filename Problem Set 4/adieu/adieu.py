import inflect

p = inflect.engine()
names = []

while True:  # keeps running until false (so keeps asking user input)
    try:
        user_input = input("Name: ").strip() # append() adds a single item to the existing list without creating a new list, instead by modifying the existing one
        names.append(user_input)
    except EOFError:
        names = p.join(names) # join() will will merge the values in the names into one sentence
        print(f'Adieu, adieu, to {names}')
        break
