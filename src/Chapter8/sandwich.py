# Exercise 8.12

def make_sandwich(*ingredients):


active = True
all_albuns = []

while active == True:
    answer = input("Would like to insert more ingredients in your sandwich? y - yes / any - no \n")
    if answer == 'y':
        ingredients = ingredients + input("Write the ingredient:* \n")
    else:
        active = False 

