from user import User

class Admin(User):
    
    def __init__(self, first_name="first_name", last_name="last_name", login_name='first_last', location='here', password='', privileges=[]):
        super().__init__(first_name, last_name, login_name, location, password)
        self.privileges = Privileges(privileges)        

class Privileges():
    
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)