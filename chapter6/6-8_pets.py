# Make several dictionaries, store them in a list.

pets = []

pet = {'animal' : 'cat',
    'name' : 'peach',
    'age' : 10,
    'owner' : 'mary',
    }
pets.append(pet)

pet = {'animal' : 'fish',
    'name' : 'dora',
    'age' : 1,
    'owner' : 'eugene',
    }
pets.append(pet)

pet = {'animal' : 'guinea pig',
    'name' : 'fluff',
    'age' : 3,
    'owner' : 'denis',
    }
pets.append(pet)

# Loop through the list, print everything about each pet.

for pet in pets:
	animal = pet['animal']
	name = pet['name']
	age = pet['age']
	owner = pet['owner']
	if age == 1:
		print(f"\n{owner.title()} has the cutest "
			f"{age} year old {animal} named {name.title()}!")
	else:
		print(f"\n{owner.title()} has the cutest "
			f"{age} years old {animal} named {name.title()}!")

for pet in pets:
	print('\nHere is all the information I have about this pet:')
	for key, pet_info in pet.items():
		if pet_info == pet['name']:
			print(f'--{key}: {pet_info.title()}')
		elif pet_info == pet['owner']:
			print(f'--{key}: {pet_info.title()}')
		else:
		    print(f'--{key}: {pet_info}')
