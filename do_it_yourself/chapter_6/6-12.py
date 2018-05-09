cities = {
    "Chicago": {"state": "Illinois", "country": "United States", "population": 3000000, "fact": "Meat packing home", "motto": "The City that Works",},
    "London": {"state": "unknown", "country": "United Kingdom", "population": 5000000, "fact": "Home of the financial center of the world",},
    "San Antonio": {"state": "Texas", "country": "United States", "population": 100000, "fact": "Tammie lives here",},
    }

for city_name, information in cities.items():
    print(city_name + " Information:")
    for key, value in information.items():
        print("\t\t", end='')
        print(key +": " + str(value))
    print("\n")