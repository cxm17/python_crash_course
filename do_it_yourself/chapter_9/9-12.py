
from domain_services import Admin

user1 = Admin("Cortez", "Mack", "cmack", "Westchester", "password123", ["delete", "add", "disconnect", "override"])
user1.describe_user()
user1.privileges.show_privileges()

