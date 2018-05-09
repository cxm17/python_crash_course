magicians = ["Whoodini", "Cooperfield", "Dillahunty"]

def show_magicians(magicians_list):

    for magician in magicians_list:
        print("Hello " + magician)

def edit_magicians(magicians):

    for index in range(0, len(magicians)):
        magicians[index] = "Great " + magicians[index]

    return magicians

great_magicians = edit_magicians(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)