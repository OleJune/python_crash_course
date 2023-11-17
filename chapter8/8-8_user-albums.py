def make_album(artist_name, album_title):
	"""Build and return a dictionary describing a music album."""
	album = {'artist': artist_name.title(), 'album': album_title.title()}
	return album

while True:
	print("\nPlease, enter your favourite artist "
	"and the title of the album you like the most:")
	print("(press 'q' to exit)")
	artist_name = input("Artist: ")
	if artist_name == 'q':
		break
	album_title = input("Album: ")
	if album_title == 'q':
		break
	info = make_album(artist_name, album_title)
	print(info)
