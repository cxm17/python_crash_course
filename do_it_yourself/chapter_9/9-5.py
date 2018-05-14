class User():
    
    def __init__(self, first_name, last_name, login_name, location, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login_name = login_name
        self.location = location
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Login Name: " + self.login_name)
        print("location: " + self.location)
        print("Number of logins: " + str(self.login_attempts))
    
    def greet_user(self):
        print("Hello, " + self.first_name + ". Your listed location is " + self.location)
    
    def login(self):
        self.login_attempts = self.login_attempts + 1
    
    def reset_logins(self):
        print("RESETTING LOGIN TOTAL...")
        self.login_attempts = 0

user1 = User("Cortez", "Mack", "cmack", "Westchester", "password123")
user1.describe_user()
user1.login()
user1.login()
user1.login()
user1.login()
user1.describe_user()
user1.reset_logins()
user1.describe_user()