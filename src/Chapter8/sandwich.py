# Exercise 8.12

def make_sandwich(*ingredients):
    print("Did you request a sandwich with: ")
    for ingredient in ingredients:
        print("- " + ingredient)


make_sandwich('Ham', 'Cheese', 'Black olive', 'Cream Cheese')

make_sandwich('Chicken', 'Carrot', 'Mayo')

make_sandwich('Egg', 'Cheese', 'Cream Cheese')

