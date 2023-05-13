def main():
    # Settings - setting variables
    amount_inserted = 0
    coke_price = 50
    coins = [5, 10, 25]

    # using while True to create a loop that keeps on running.
    while True:
        # coin_inserted += will add to whatever amount inserted in input
        coin_inserted = int(input("Insert one coin at a time: ").replace('"', '').replace("'", '').strip()) # accepts strings and removes spaces
        if coin_inserted not in coins:#Conditional for invalid input
            print("Invalid coin. Amount due: 50")
            continue # loop continues

        amount_inserted += coin_inserted # keeps track of what was inserted and continues counting (ingnores invalid coins)

        if amount_inserted > coke_price: # conditional if/else statement
            print(f"Change owed: {amount_inserted - coke_price}, enjoy your coke!")
            return # exiting loop if above condition met, else continues
        elif amount_inserted == coke_price:
            print(f"Change owed: {amount_inserted - coke_price}, enjoy your coke!")
            return # exiting loop if above contition met, else continues
        else:
            print(f"Amount due: {coke_price - amount_inserted}")


main()
