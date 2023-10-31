favourite_numbers = {'emma' : 3, 'ted' : 7, 'pit' : 13, 'ann' : 99, 'jay' : 40}
number = favourite_numbers['emma']
print(f"Emma's favourite number is {number}.")

number = favourite_numbers['ted']
print(f"Ted's favourite number is {number}.")

number = favourite_numbers['pit']
print(f"Pit's favourite number is {number}.")

number = favourite_numbers['ann']
print(f"Ann's favourite number is {number}.")

number = favourite_numbers['jay']
print(f"Jay's favourite number is {number}.")

# Variant 2: this code is easier to modify, so it's more efficient.

name = 'emma'
number = favourite_numbers[name]
print(f"\n{name.title()}'s favourite number is {number}")

name = 'ted'
number = favourite_numbers[name]
print(f"{name.title()}'s favourite number is {number}")

name = 'pit'
number = favourite_numbers[name]
print(f"{name.title()}'s favourite number is {number}")

name = 'ann'
number = favourite_numbers[name]
print(f"{name.title()}'s favourite number is {number}")

name = 'jay'
number = favourite_numbers[name]
print(f"{name.title()}'s favourite number is {number}")
