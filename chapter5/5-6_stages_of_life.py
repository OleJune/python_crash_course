# Write an if-elif-else chain that determines a person's stage of life

age = 77

if age < 2:
	life_stage = 'a baby'
elif age < 4:
	life_stage = 'a toddler'
elif age < 13:
	life_stage = 'a kid'
elif age < 20:
	life_stage = 'a teenager'
elif age < 65:
	life_stage = 'an adult'
else:
	life_stage = 'an elder'

print(f'A person is {life_stage}.')
