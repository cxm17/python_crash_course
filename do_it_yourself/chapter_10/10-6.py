user_input = input("Enter 1st number: ")

try:
    number_1 = int(user_input)
except ValueError:
    print(user_input + " is not a integer")
else:
    print(number_1)
