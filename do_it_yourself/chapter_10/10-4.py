active = True
file_name = "guest_book.txt"

with open(file_name, "a") as file_object:
    while active:
        new_name = input("Please enter a name: ")
        if new_name == "*":
            print("Thank you! Please check " + file_name + " for accuracy.")
            active = False
        else:
            file_object.write(new_name + "\n")
    