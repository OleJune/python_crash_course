prompt = input("Good evening! How many people are there in your group? ")
number = int(prompt)

if number > 8:
	print("Sorry, you will have to wait for a table.")
else:
	print("Please, follow me. Your table is ready.")
