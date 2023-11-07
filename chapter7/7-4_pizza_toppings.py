prompt = "\nWhat topping would you like to add to your pizza?"
prompt += "\n(When you are done with toppings, enter 'quit') "
topping = ""

while topping != 'quit':
	topping = input(prompt)
	if topping != 'quit':
		print(f"I'll add {topping} to your pizza.")
