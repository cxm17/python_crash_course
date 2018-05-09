def make_album(artist_name, album_name, number_of_tracks = None):
    
    album = dict()

    album[artist_name] = album_name

    if number_of_tracks:
        album["Tracks"] = number_of_tracks
    
    return album

active = True

while active:

    artist_name = input("Please enter an artist name (or \"quit\" to exit)-> ")

    if artist_name.lower() == 'quit':
        break

    album_name = input("Please enter an album name-> ")

    album = make_album(artist_name, album_name)

    print(album)