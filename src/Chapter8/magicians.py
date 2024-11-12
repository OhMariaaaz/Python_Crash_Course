# Exercise 8.9, 8.10 and 8.11

def show_magicians(magicians):
    for magician in magicians:
        print(magician  + "\n")
    print("\n")

def make_great(magicians):
    for magician in magicians:
        magicians.remove(magician)
        magicians.insert(0, "The great " + magician)
    print("\n")


magicians = []
active = True

while active == True:
    answer = input("Would like to create a new magician? y - yes / any - no \n")
    if answer == 'y':
        name = input("Write the name of the magician:* \n")
        if name == '':
            print("\n" + "Error! Please fill in all the necessary information."+ "\n")
        else:
            magicians.append(name)
    else:
        active = False

show_magicians(magicians)

make_great(magicians[:])
show_magicians(magicians)

make_great(magicians)
show_magicians(magicians)