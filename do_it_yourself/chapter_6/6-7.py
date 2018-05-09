person1 = {"first_name": "Jeffery", "last_name": "Brooke", "age": 44, "city": "Tinley Park"}
person2 = {"first_name": "Traci", "last_name": "Brooke", "age": 42, "city": "Tinley Park"}
person3 = {"first_name": "Marci", "last_name": "Scott", "age": 48, "city": "Los Angeles", "job": "Fitness Trainer"}

people = [person1, person2, person3]

for person in people:
    print("********************************")
    for key, value in person.items():
        print(key + " = " + str(value))