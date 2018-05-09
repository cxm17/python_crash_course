pet1 = {"Name": "Brian", "Owner": "Peter", "Type": "Dog"}
pet2 = {"Name": "Lassie", "Owner": "Billy", "Type": "Dog"}
pet3 = {"Name": "Mack", "Owner": "Corky", "Type": "Cat"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("-----------------------")
    for key, value in pet.items():
        print(key + " = " + value)