sandwich_orders = []

sandwich_orders.append('ham sandwich')
sandwich_orders.append('hummus sandwich')
sandwich_orders.append('avocado sandwich')
sandwich_orders.append('chicken sandwich')

finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"\nHere's your {current_sandwich}. Enjoy!")
	finished_sandwiches.append(current_sandwich)
	
print(f"\nI made the following sandwiches:")
for sandwich in finished_sandwiches:
	print(f"--{sandwich}")
