def make_album(artist_name, album_name, number_of_tracks = None):

    album = dict()

    album[artist_name] = album_name

    if number_of_tracks:
        album["Tracks"] = number_of_tracks
    
    return album

album = make_album("Bobby Digital", "Silver Bullets")
print(album)

album = make_album("Bobby Digital", "Gold Bullets", 9)
print(album)