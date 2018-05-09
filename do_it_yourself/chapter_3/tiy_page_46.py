#3-4

guests = ['Daylyt', 'Pinky', 'Thomas Payne']
message = ", you are invited to dinner."
print(guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)
print("Guest list: " + str(guests))

#3-5

print(guests.pop(1) + " cannot make it to the dinner. She will send her represenative.")
guests.insert(1, "Nini Rotti")
print(guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)
print("New guest list: " + str(guests))

#3-6

print("We are inviting more people!")
guests.insert(0, "Gizelle")
guests.insert(2, "Honey Gold")
guests.append("Kitten")
print(guests[3] + message)
print(guests[4] + message)
print(guests[5] + message)
print("New guest list: " + str(guests))

#3-7
print("Oops! We do not have enough food!")
print(guests.pop() + " stay home!")
print(guests.pop() + " stay home!")
print(guests.pop() + " stay home!")
print(guests.pop() + " stay home!")
print("New guest list: " + str(guests))
##remove last two people
print("I am cancelling the whole thing!")
del guests[0]
del guests[0]
print("New guest list: " + str(guests))
