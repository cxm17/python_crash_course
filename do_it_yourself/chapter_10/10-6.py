active = True

while active:

    try:
        x = int(input("Enter first number: "))

    except ValueError:
        print("Not a number!")
        break

    try:
        y = int(input("Enter second number: "))
    except ValueError:
        print("Not a number!")
        break

    print(str(x + y))

print("Good Bye!")