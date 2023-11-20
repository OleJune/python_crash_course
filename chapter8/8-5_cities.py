def describe_city(city_name, country_name='ukraine'):
	"""Print a sentance describing a city."""
	print(f"\n{city_name.title()} is in {country_name.title()}.")

describe_city('lviv')
describe_city(city_name='odesa')
describe_city('london', 'england')
describe_city(country_name='england', city_name='london')
