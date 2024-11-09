# Exercises 7.4 and 7.6

add_ingredient = 'active'
my_pizza = ['dough', 'tomato sauce']
while add_ingredient == 'active':
    answer = input("What ingredient do you want in you pizza? (write 'quit' to exit!) ")

    if answer != 'quit':
        my_pizza.append(answer)
        print("Adding " + answer + " to your pizza.")
        print("That's your pizza: \n" + str(my_pizza))
    else:
        add_ingredient = 'end'
        print("That's your pizza: \n" + str(my_pizza))
        break
