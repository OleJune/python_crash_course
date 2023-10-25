print('1. Tests for equality and inequality with strings:')
food = 'pizza'
if food != 'pasta':
	print(f'I love {food}.')
	print(food != 'pasta')
if food == 'pizza':
	print(f'{food.title()} is my favourite food.')
	print(food == 'pizza')

print('\nTests for equality and inequality with strings:')

# Looping through the list

foods = ['pizza', 'pasta', 'lasagna']
for food in foods:
    if food != 'pasta':
	    print(f'I love {food}.')
    else:
	    print(f'{food.title()} is my favourite food.')

print('\n2. Test using the lower() method:')
planet = 'Earth'
print("Is planet == 'Earth'? I predict True.")
print(planet.lower() == 'earth')


print('\n3. Numerical tests:')
number = 15
number_1 = 20
if number != number_1:
	print("That's right! 15 is not equal to 20.")

# Looping through the list

numbers = [3, 6, 9, 12, 15]
for number in numbers:
	if number == 6:
		print(f'3 + 3 equals {number}.')
	if number != 15 and number != 12:
		print(f'{number} is a one-digit number.')
	if number > 12:
		print(f'{number} is greater than 12.')
	if number < 6:
		print(f'{number} is less than 6.')
	if number >= 15:
		print(f'{number} is the greatest number in the list.')
	if number <= 3:
		print(f'{number} is the smallest number in the list.')
	if number < 12 and number > 6:
		print(f'{number} is less than 12 and is greater than 6.')
	if number <= 99 or number >= 10:
		print(f'{number} is a two-digit number.')

print('\n4. Tests using the -and- and the -or- keywords:')
reptile = 'snake'
reptile_1 = 'turtle'
print("Is reptile == 'snake' and reptile_1 == 'lizard' ? I predict False.")
print(reptile == 'snake' and reptile_1 == 'lizard')
print(f"Reptile_1 is a {reptile_1}.")

dessert = 'cake'
dessert_1 = 'pie'
print("\nIs dessert == 'cake' or dessert_1 == 'cheesecake'? I predict True.")
print(dessert == 'cake' or dessert_1 == 'cheesecake')
print(f'Dessert == {dessert}, dessert_1 == {dessert_1}.')

print('\n5. Test whether an item is in a list:')
seasons = ['summer', 'winter', 'autumn', 'spring']
print('I wonder if summer is in a list? I predict True.')
print('summer' in seasons)

print('\n6. Test whether an item is not in a list:')
citruses = ['grapefruit', 'lemon', 'orange']
print("There is no lemon in a list. I predict False.")
print('lemon' not in citruses)

print('\nTest whether an item is not in a list:')
citruses = ['grapefruit', 'lemon', 'orange']
fruit = 'lime'
if fruit not in citruses:
    print(f'There is no {fruit} in a list.')
    print(fruit not in citruses)
