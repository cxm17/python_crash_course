favorite_languages = {
    "Cortez": "Java",
    "Bobby": "T-SQL",
    "John": "C#",
    "Jim": "Pascal"
}

candidates = {
    "John",
    "Ed",
    "Cortez",
    "Joe",
    "Benny"
}

for candidate in candidates:
    if candidate in favorite_languages.keys():
        print("Thanks for taking the poll, " + candidate + "!")
    else:
        print(candidate + ", please give us your information!")