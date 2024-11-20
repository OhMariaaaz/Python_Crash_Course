# Exercise 9.1

class Restaurant(): 
    '''Creating a restaurant object!'''
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a restaurant of " + self.cuisine_type.title() + ". And it already" +
              " served " + str(self.number_served) + " customers!")
        return

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")
        return
    
    def set_number_served(self, number_served):
        self.number_served = number_served
        print(self.restaurant_name.title() + " was updated!")


    def increment_number_served(self, number_served):
        self.number_served = self.number_served + number_served
        print(self.restaurant_name.title() + " has attended more " + str(number_served) + " customers!")
    

'''
my_restaurant = Restaurant("Pé de Fava", "Nordestino")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
'''
        
