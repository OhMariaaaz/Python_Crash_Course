# Exercise 8.7 and 8.8

def make_album(name, artist, year = "0000"):
    new_album = {'name': name, 'artist': artist, 'year': year}
    return new_album

active = True
all_albuns = []

while active == True:
    answer = input("Would like to create a new album? y - yes / any - no \n")
    if answer == 'y':
        name = input("Write the name:* \n")
        artist = input("Write the artist:* \n")
        year = input("Write the year: \n")
        if name == '' or artist == '':
            print("\nError! Please, fill in all the required information.\n")
        elif year == '':
            all_albuns.append(make_album(name, artist)) 
        else:
            all_albuns.append(make_album(name, artist, year))
    else:
        active = False

print(all_albuns)
