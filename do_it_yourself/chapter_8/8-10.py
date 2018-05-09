magicians = ["Whoodini", "Cooperfield", "Dillahunty"]

def show_magicians(magicians_list):

    for magician in magicians_list:
        print("Hello " + magician)

def great_magicians(magicians):

    for index in range(0, len(magicians)):
        magicians[index] = "Great " + magicians[index]

great_magicians(magicians)
show_magicians(magicians)