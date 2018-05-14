class User():

    def __init__(self, first_name, last_name, login_name, location, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login_name = login_name
        self.location = location
        self.password = password

    def describe_user(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Login Name: " + self.login_name)
        print("location: " + self.location)
    
    def greet_user(self):
        print("Hello, " + self.first_name + ". Your listed location is " + self.location)

user1 = User("Cortez", "Mack", "cmack", "Westchester", "password123")
user2 = User("Betty", "Mack", "bmack", "North Carolina", "password987")
user3 = User("John", "Mack", "jmack", "Maine", "password456")
user4 = User("Eddie", "Mack", "emack", "West Haven", "password091")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()