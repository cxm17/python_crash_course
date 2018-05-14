from random import randint

class Die():

    def __init__(self, number_of_sides=6):
        self.sides = number_of_sides

    def roll_die(self):
        
        side_rolled = randint(1, self.sides)
        print(side_rolled)

die = Die()

for x in range(1, 11):
    print("Roll " + str(x) +": ", end='')
    die.roll_die()

die = Die(10)

for x in range(1, 11):
    print("Roll " + str(x) +": ", end='')
    die.roll_die()


die = Die(20)

for x in range(1, 11):
    print("Roll " + str(x) +": ", end='')
    die.roll_die()