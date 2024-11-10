# Exercise 8.1 e 8.2

def message(name = "user", game = "chess"):
    print("Welcome, " + name + "! \nLet's play " + game + "!!!")
    return 

name = input("Write your name: \n")
favorite_game = input("Your favorite game: \n")
message(name, favorite_game)
