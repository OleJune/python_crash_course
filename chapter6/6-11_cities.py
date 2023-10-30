cities = {
	'toronto' : {
	'country' : 'canada',
	'population' : 2_800_000,
	'fact' : 'most populous city',
	},
	'québec' : {
	'country' : 'canada',
	'population' : 550_000,
	'fact' : 'french speaking province',
	},
	'ottawa' : {
	'country' : 'canada',
	'population' : 1_017_000,
	'fact' : "country's capital",
	},

	}

for city, city_info in cities.items():
	print(f'\nThis is {city.title()}.')
	country = city_info['country']
	popul = city_info['population']
	fact = city_info['fact']
	print(f'Here is some information about it:')
	print(f'country: {country}')
	print(f'population: {popul}')
	print(f'fact: {fact}')


for city, city_info in cities.items():
	print(f'\nThis is {city.title()}.')
	full_info = f"country: {city_info['country']}\npopulation: {city_info['population']}\nfact: {city_info['fact']}"
	print(f'Here is some information about it:')
	print(f'{full_info}')


