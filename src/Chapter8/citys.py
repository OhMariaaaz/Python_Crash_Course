# Exercise 8.5, 8.6

def describe_city(country = "default", city = "default"):
    print(city + ", " + country + ".")
    return


country = input("What is the country? \n")
city = input("What is the city? \n")


if country != "":
    if city != "":
        describe_city(country, city)
    else:
        describe_city(country = country)
elif city != "":
    describe_city(city = city)
else:
    describe_city()