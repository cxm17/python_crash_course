favorite_places = {"Corky": ["Home", "Courts"], "Jeffery": ["Las Vegas", "Trail", "Moon"], "Krystal": ["Texas"]}

for key, value in favorite_places.items():
    print(key + " likes the following places:")
    for place in value:
        print(place)