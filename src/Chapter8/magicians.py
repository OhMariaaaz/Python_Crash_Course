# Exercise 8.7 and 8.8

def show_magicians(magicians):
    for magician in magicians:
        print(magician)
    return magicians

def make_great(magicians):
    for magician in magicians:
        magician = "The Great " + str(magician) 
        print(magician + "\n")
    return magicians


active = True
magicians = []

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

show_magicians(magicians[:])

magicians_copy = magicians[:]
make_great(magicians_copy[:])

print("Original list"+ str(magicians) + "\n")
print("Copy list"+ str(magicians_copy) + "\n")