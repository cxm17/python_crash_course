get_reasons = True
file_name = "reasons.txt"

def ask_for_reasons(name, file_object):
    
    active = True

    while active:
        new_reason = input("Please enter your reason: ")
        if new_reason == "*":
            return
        else:
            file_object.write(name + " said " + new_reason + "\n")


with open(file_name, "a") as file_object:
    while get_reasons:
        new_name = input("Please enter a name: ")
        if new_name == "*":
            get_reasons = False
        else:
            ask_for_reasons(new_name, file_object)
