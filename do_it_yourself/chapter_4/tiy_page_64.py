# 4-3
for value in range(1, 21):
    print(value)

# 4-4
# numbers = list(range(1, 1000001))
numbers = list(range(1, 1000001, 100000))

for number in numbers:
    print(number)

#4-5
numbers = list(range(1, 1000001))
print("sum of integers between 1 - 1000000: " + str(sum(numbers)))

#4-6
for value in range(1, 20, 2):
    print(value)

#4-7
print("")
for value in range(3, 30, 3):
    print(value)

#4-8
print("Cubes: Using loop")
cubes = []
for value in range(1,11):
    cubes.append(value**3)

for cube in cubes:
    print(cube)

#4-9
print("Cubes: List comprehension")
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)