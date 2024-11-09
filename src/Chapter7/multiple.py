# Exercises 7.3

number = int(input("Write a number: "))

rest = number % 10

if rest == 0:
    print(str(number) + " it's a multiple of ten.")
else:
    print(str(number) + " isn't a multiple of ten.")