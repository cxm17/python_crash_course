sandwich_orders = ["Corned Beef", "Turkey", "Roast Beef", "Burger"]
finished_sandwiches = list()

while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)


for sandwich in finished_sandwiches:
    print("Pickup your " + sandwich + ". Thanks for your business!")

print(sandwich_orders)