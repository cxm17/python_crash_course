sandwich_orders = ["Corned Beef", "Turkey", "Roast Beef", "Burger", "Pastrami", "Pastrami", "Pastrami"]

print("Here are the current orders" + str(sandwich_orders))
print("We are out of Pastrami! Removing those orders...")

order_to_be_removed = 'Pastrami'

while order_to_be_removed in sandwich_orders:
        sandwich_orders.remove(order_to_be_removed)

print("Here are the current orders" + str(sandwich_orders))