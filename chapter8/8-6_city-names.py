def city_country(city, country):
	"""Return a string formatted like this: Santiago, Chile."""
	full_info = f"\n{city}, {country}"
	return full_info.title()

travel_info = city_country('oslo', 'norway')
print(travel_info)

travel_info = city_country('helsinki', 'finland')
print(travel_info)

travel_info = city_country('stockholm', 'sweden')
print(travel_info)
