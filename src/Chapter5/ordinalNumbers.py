# Exercises 5.11

ordinal_numbers = range(1,10)

for number in ordinal_numbers:
    if(number == 1):
        print(str(number) + "st")
    elif(number == 2):
        print(str(number) + "nd")
    elif(number == 3):
        print(str(number) + "rd")
    else:
        print(str(number) + "th")