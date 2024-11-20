# Exercise 9.2

from restaurant import Restaurant

restaurants = {}
restaurants['Fogo de Chão'] = Restaurant("Fogo de Chão", "Brazilian barbecue (Rodízio)")
restaurants['Oro'] = Restaurant("Oro", "Contemporary Brazilian cuisine")
restaurants['D.O.M.'] = Restaurant("D.O.M.", "Brazilian fine dining")

for restaurant in restaurants.values():
            restaurant.describe_restaurant()
            restaurant.open_restaurant()
            print("\n")

restaurants['Fogo de Chão'].set_number_served(1658)
print("\n")
restaurants['Oro'].set_number_served(3054)
print("\n")
restaurants['D.O.M.'].set_number_served(2645)
print("\n")

for restaurant in restaurants.values():
            restaurant.describe_restaurant()
            restaurant.open_restaurant()
            print("\n")

restaurants['Fogo de Chão'].increment_number_served(1645)
print("\n")
restaurants['D.O.M.'].increment_number_served(541)
print("\n")

for restaurant in restaurants.values():
            restaurant.describe_restaurant()
            restaurant.open_restaurant()
            print("\n")

