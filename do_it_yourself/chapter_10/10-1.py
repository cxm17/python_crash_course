print("-------------------------------------------")

with open("learning_python.txt") as file_object:
    contents = file_object.read()
    print(contents)

print("-------------------------------------------")

with open("learning_python.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

print("-------------------------------------------")

with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
