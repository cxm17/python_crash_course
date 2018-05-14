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

class Admin(User):
    
    def __init__(self, first_name="first_name", last_name="last_name", login_name='first_last', location='here', password='', privileges=[]):
        super().__init__(first_name, last_name, login_name, location, password)
        self.privileges = privileges        

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

user1 = Admin("Cortez", "Mack", "cmack", "Westchester", "password123", ["delete", "add", "disconnect", "override"])
user1.describe_user()
user1.show_privileges()