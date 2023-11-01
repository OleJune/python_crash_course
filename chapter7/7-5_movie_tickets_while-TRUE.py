age = "\nTell me your age, and I will name the ticket price. "
age += "(To quit the program enter 'stop'.) "
#answer = ""    # this line is necessary in case we use a conditional test

while True:            # a conditional test: while answer != 'stop':
	answer = input(age)
	if answer == 'stop':   # if use a conditional test: if answer != 'stop': 
		break
	answer = int(answer)
	if answer < 3:
		print("The ticket is free.")
	elif answer < 12:
		print("The ticket costs $10.")
	else:
		print("The ticket costs $15.")
