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

class IceCreamStand(Restaurant):
    
    def __init__(self, name='new_ice_cream_stand', cuisine='ice_cream', number_served=0, flavors=[]):
        super().__init__(name, cuisine, number_served)
        self.flavors = flavors

    def display_flavors(self):
        
        for flavor in self.flavors:
            print("We serve: " + flavor)

    def describe_restaurant(self):
        super().describe_restaurant()
        self.display_flavors()
        
new_restaurant = IceCreamStand("Fred's Cones","Ice Cream", 0, ["Vanilla", "Chocolate", "Strawberry"])
new_restaurant.describe_restaurant()
