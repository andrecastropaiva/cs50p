# dictionary of fruits
items = {
        'apple': 130,
        'avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew melon': 50,
        'kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pinneaple': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerines': 50,
        'watermelon': 80
        }

# Asks user for the item
user_input = input("Item: ").lower() # lower() converts upper into lowercase

# conditionals if in
if user_input in items:
    print(f"Calories: {items[user_input]}")
# without else the program ignores invalid inputs as required...