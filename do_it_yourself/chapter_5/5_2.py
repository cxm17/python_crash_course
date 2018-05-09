string1 = "Happy"
string2 = "Pappy"
string3 = "hAPPy"
string4 = "Happy"
number1 = 10
number2 = 20
number3 = 10
items = ["Pinky", "Gizelle", "Caramel"]

print("Is " + string1 + " equal to " + string2 + "? " + str(string1 == string2))
print("Is " + string1 + " equal to " + string4 + "? " + str(string1 == string4))
print("Is " + string1 + " equal to " + string3 + " with lower() applied? " + str(string1.lower() == string4.lower()))
print("Is " + str(number1) + " equal to " + str(number2) + "? " + str(number1 == number2))
print("Is " + str(number1) + " not equal to " + str(number2) + "? " + str(number1 != number2))
print("Is " + str(number1) + " less than " + str(number2) + "? " + str(number1 < number2))
print("Is " + str(number1) + " greater than " + str(number2) + "? " + str(number1 > number2))
print("Is " + str(number1) + " greater than " + str(number2) + " and equal to " + str(number3) + "? " + str(number1 > number2 and number1 == number3))

print("Is Belladonna in " + str(items) + "? " + str("Belladonna" in items))
print("Is Caramel in " + str(items) + "? " + str("Caramel" in items))
