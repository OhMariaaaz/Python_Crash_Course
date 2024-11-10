# Exercise 8.3 and 8.4


def make_shirt(size = "large", stamp = "I love Python!"):
    print("Making a new shirt! UwU \nSize: " + size + ". \nStamp: " + stamp + ".")
    return 

size = input("What your size? \n")
stamp = input("What stamp do you like? \n")


if size != "":
    if stamp != "":
        make_shirt(size, stamp)
    else:
        make_shirt(size = size)
elif stamp != "":
    make_shirt(stamp = stamp)
else:
    make_shirt()

