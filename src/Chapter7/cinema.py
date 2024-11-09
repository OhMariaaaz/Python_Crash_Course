# Exercises 7.5 and 7.7
party = int(input("Welcome to the cinemark! How many tickets do you want?"))
i = 1
total_value = 0

while i <= party:
    age = int(input("How old are the " + str(i) + "° person in your party?"))

    if age > 12:
        print("15 dollars the ticket")
        total_value = total_value + 15
    elif age > 3:
        print("10 dollars the ticket")
        total_value = total_value + 10
    else:
        print("Free!")

    i = i + 1

print("total: " + str(total_value) + " dollars")

'''
while i != 0:
    print("bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!bug!")
'''