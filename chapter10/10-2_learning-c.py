file = 'learning_python.txt'

with open(file) as file_object:
	for line in file_object:
		print(line.replace('Python', 'C').strip())


file = 'learning_python.txt'

with open(file) as file_object:
    for line in file_object:
        new_line = line.replace('Python', 'C')
        print(new_line.strip())
