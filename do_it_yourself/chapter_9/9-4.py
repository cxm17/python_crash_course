class Restaurant():
    
    def __init__(self, name='new_restaurant', cuisine='standard_cuisine', number_served=0):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = number_served
    
    def describe_restaurant(self):
        print("Name: " + self.restaurant_name)
        print("Menu/Cuisine: " + self.cuisine_type)
        print("Number served: " + str(self.number_served))

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")

    def set_number_served(self, number_of_customers=0):
        self.number_served = number_of_customers

    def increment_number_served(self):
        self.number_served = self.number_served + 1

new_restaurant = Restaurant("Fred's furters", "Hot Dogs", 0)
new_restaurant.describe_restaurant()
new_restaurant.increment_number_served()
new_restaurant.increment_number_served()
new_restaurant.increment_number_served()
new_restaurant.describe_restaurant()
new_restaurant.number_served = 20998
new_restaurant.describe_restaurant()