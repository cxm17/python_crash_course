age = None
active = True

while active:
    age = input("What is your age? ")

    if age.lower() == 'quit':
        print("good bye!")
        break

    age = int(age)

    if age < 3:
        print("Your ticket cost is $0...")
    elif age >= 3 and age <= 12:
        print("Your ticket cost is $10...")
    elif age >= 12:
        print("Your ticket cost is $15...")