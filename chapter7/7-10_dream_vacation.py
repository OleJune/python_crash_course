poll_results = {}

prompt = "Please, name one place in the world you'd like to visit the most: "

poll_active = True

while poll_active:
	name = input("What is your name? ")
	place = input(prompt)
	poll_results[name] = place

	yes_no = input("Someone else wants to take a poll? (y / n) ")
	if yes_no == 'n':
		poll_active = False

print("\nHere's the results of the poll:\n")
for name, place in poll_results.items():
	print(f"--Name: {name.title()}  --Place: {place.title()}")
