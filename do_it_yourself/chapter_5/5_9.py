user_names = ["cmack", "jbrooke", "sturner", "smaribelli", "jcashmere", "admin"]

for count in range(1,3):
    
    print(str(user_names) + " loop count " + str(count))

    if user_names:
        for user_name in user_names:
            if user_name == "admin":
                print("Hello, " + user_name + " would you like to see a systems report?")
            else:
                print("Hello " + user_name + " welcome to the system.")    
    else:
        print("We need to find some users!")

    user_names = []



