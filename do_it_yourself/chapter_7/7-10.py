vacations = []

ask_about_vacations = True

while ask_about_vacations:

    user_input = input("Where would you love to go for vacation-> ")
    
    if user_input.lower() == "quit":
        break
    
    vacations.append(user_input)

for vacation in vacations:
    print("You would like to go to " + vacation + "! Great!")