# 4-10

film_stars = ["Jessica Bangkok", "Honey Gold", "Kitten", "Caramel", "Kiara Mia"]

print("The first three messages in the list are :")
for film_star in film_stars[:3]:
    print("\t", end='')
    print(film_star)
print("The middle three messages in the list are :")
for film_star in film_stars[1:4]:
    print("\t", end='')
    print(film_star)
print("The last three messages in the list are :")
for film_star in film_stars[-3:]:
    print("\t", end='')
    print(film_star)

# 4-11

pizza_types = ["Sauage/Pepperoni", "Cheese", "Deep Dish Junk"]

friends_pizzas = pizza_types[:]

pizza_types.append("Pineapple")
friends_pizzas.insert(1, "Ham/Anchovies")

print("My favorite pizzas are:")
for pizza in pizza_types:
    print("\t", end='')
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print("\t", end='')
    print(pizza)

# 4-12

my_foods = ["oatmeal cookies", "beef hot links", "eli's cheesecake"]
friend_foods = my_foods[:]
friend_foods.insert(0, "ketchup")
friend_foods.pop(-1)
friend_foods.pop(-1)
friend_foods.pop(-1)

print("My favorite foos are:")
for food in my_foods:
    print("\t", end='')
    print(food)

print("My friend's favorite foods are:")
for food in friend_foods:
    print("\t", end='')
    print(food)
