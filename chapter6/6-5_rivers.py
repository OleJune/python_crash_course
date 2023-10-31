rivers = {
    'dnipro' : 'ukraine',
    'thames' : 'england',
    'sein' : 'france',
    }

# Looping through all key-value pairs

for river, country in rivers.items():
	print(f'{river.title()} is the major river of {country.title()}.')

# Looping through all keys
print('\nName of each river:')
for river in rivers.keys():
	print(f'{river.title()}')

# Looping through all values
print('\nName of each country:')
for country in rivers.values():
	print(f'{country.title()}')
