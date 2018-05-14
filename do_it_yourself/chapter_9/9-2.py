class Restaurant():
    
    def __init__(self, name='new_restaurant', cuisine='standard_cuisine'):
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        print("Name: " + self.restaurant_name)
        print("Menu/Cuisine: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")

restaurant1 = Restaurant()
restaurant2 = Restaurant("Portillo's", "Americans")
restaurant3 = Restaurant("Ruth's Chris", "Steakhouse")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()