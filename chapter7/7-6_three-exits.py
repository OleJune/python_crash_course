# Use a conditional test in the while statement to stop the loop.

prompt = "\nWhat topping would you like to add to your pizza?"
prompt += "\n(When you are done with toppings, enter 'quit') "
message = ""

while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(f"I'll add {message} to your pizza.")

# Use an active variable to control how long the loop runs.

prompt = "\nWhat topping would you like to add to your pizza?"
prompt += "\n(When you are done with toppings, enter 'quit') "

active = True

while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(f"I'll add {message} to your pizza.")

# Use a break to exit the loop when the user enters a 'quit' value.

prompt = "\nWhat topping would you like to add to your pizza?"
prompt += "\n(When you are done with toppings, enter 'quit') "

while True:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(f"I'll add {message} to your pizza.")
