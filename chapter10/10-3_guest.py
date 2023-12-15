filename = 'guest.txt'
prompt = "Please, tell me your name: "

with open(filename, 'w') as file_object:
	name = input(prompt)
	file_object.write(f"{name.title()}\n")
