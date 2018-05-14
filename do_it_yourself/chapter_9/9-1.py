class Restaurant():

    def __init__(self, name='new_restaurant', cuisine='standard_cuisine'):
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        print("Name: " + self.restaurant_name)
        print("Menu/Cuisine: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")

new_restaurant = Restaurant()
print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_type)
new_restaurant.open_restaurant()
new_restaurant.describe_restaurant()
