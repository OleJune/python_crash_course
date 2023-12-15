# Print the contents by reading in the entire file.

with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

# Print the contents by looping over the file object.

filename = 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())

print('')

# Print the contents by storing the lines in a list.

filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(line.strip())
