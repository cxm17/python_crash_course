favorite_numbers = {"Cortez": [17, 2, 7], "Christopher": [3], "Jeffery":  [5, 23], "Larry Bird": [33]}

for key, value in favorite_numbers.items():
    print(key + "'s favorite nubmers are:")
    for item in value:
        print(item)