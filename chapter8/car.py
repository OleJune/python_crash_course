def car_profile(manufacturer, model_name, **car_info):
	"""Build a dictionary that stores information about a car."""
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model_name
	return car_info

car = car_profile('audi', 'a5', color='silver', year='2020')

print(car)
