prompt = "\nWhy do you like programming? (press 'q' to exit): "
filename = 'prog_poll.txt'

while True:
    answer = input(prompt)
    if answer == 'q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(f"{answer}\n")
