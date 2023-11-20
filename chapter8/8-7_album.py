def make_album(artist_name, album_title, n_songs=None):
	"""Build and return a dictionary describing a music album."""
	album = {'artist': artist_name.title(), 'album': album_title.title()}
	if n_songs:
		album['number of songs'] = n_songs
	return album

album_info = make_album('stromae', 'racine carrée')
print(album_info)

album_info = make_album('red hot chili peppers', 'the getaway')
print(album_info)

album_info = make_album('adele', '30', '12')
print(album_info)
