# Exercise 7.10

votes = []
keep_voting = True
while keep_voting == True:
    answer = input("Do you like to vote? y - yes / v - view votes / any - no \n")
    if answer == "y":
        votes.append(input("If you could visit any place in the world, where would you like to go? \n"))
    elif answer == "v":
        print(votes)
    else:
        print(votes)
        keep_voting = False
        break 

