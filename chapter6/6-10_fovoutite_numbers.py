favourite_numbers = {'emma' : [3, 13, 33],
    'ted' : [7, 0, 11],
    'pit' : [6, 23],
    'ann' : [99],
    'jay' : [1, 40, 55],
    }

for name, numbers in favourite_numbers.items():
	if len(numbers) == 1:
		print(f"\n{name.title()}'s' favourite number is: ")
	else:
		print(f"\n{name.title()}'s' favourite numbers are: ")
	for number in numbers:
		print(f'{number}')
