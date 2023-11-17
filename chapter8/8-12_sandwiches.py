def make_sandwich(*toppings):
	"""Print a summary of the sandwich naming all the toppings added."""
	print("\nHere is your sandwich with the following toppings:")
	for topping in toppings:
		print(f"--{topping}")

make_sandwich('onion', 'herrings')
make_sandwich('egg', 'mushrooms', 'avocado')
make_sandwich('salami')
