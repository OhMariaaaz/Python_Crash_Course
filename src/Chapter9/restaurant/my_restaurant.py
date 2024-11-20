# Exercise 9.2

from restaurant import *

restaurants = []
restaurants.append(Restaurant("Fogo de Chão", "Brazilian barbecue (Rodízio)"))
restaurants.append(Restaurant("Oro", "Contemporary Brazilian cuisine"))
restaurants.append(Restaurant("D.O.M.", "Brazilian fine dining"))

for restaurant in restaurants:
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
