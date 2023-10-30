favourite_places = {
    'alice' : ['machu picchu', 'iguazu falls'],
    'alex' : ['perito moreno glacier'],
    'amy' : ['lake titikaka', 'milford sound', 'bromo'],
    }

for name, places in favourite_places.items():
	print(f'\n{name.title()} was mesmerized by the beauty of those places:')
	for place in places:
		print(f'\t {place.title()}')

# Modify the code to make the output more correct.
# Use if statement to check whether there is one favourite place or more.

print('\n--Print separate message if there is only one favourite place--')

for name, places in favourite_places.items():
	if len(places) == 1:
		print(f'\n{name.title()} was mesmerized by the beauty of this place:')
	else:
		print(f'\n{name.title()} was mesmerized by the beauty of those places:')
	for place in places:
		print(f'\t {place.title()}')
