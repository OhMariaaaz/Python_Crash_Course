# Exercise 7.8 and 7.9

sandwich_orders = []
finished_sandwich = []

order = int(input("How many sandwichs do you want?"))

while order > 0:
    sandwich_orders.append(input("Which sandwich would you like?"))
    order = order - 1

print("You have ordered: " + str(sandwich_orders))

print("We don't have pastrami anymore!")

sandwich_orders = [sandwich for sandwich in sandwich_orders if 'pastrami' not in sandwich]

while len(sandwich_orders) > 0:
    print("You sandwich " + str(sandwich_orders[0]) + " is ready!")
    finished_sandwich.append(sandwich_orders.pop(0))
    

print(sandwich_orders)
print(finished_sandwich)
