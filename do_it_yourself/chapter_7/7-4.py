user_input = ''

while True:
    user_input = input("What topping would you like on your pizza? ")
   
    if user_input.lower() == 'quit':
        print("Going to make your pizza now!")
        break
    
    print("Adding " + user_input + " to your pizza...")