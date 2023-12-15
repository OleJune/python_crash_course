prompt = "\nPlease, tell me your name (press 'q' to exit): "
filename = 'guest_book.txt'

while True:
    answer = input(prompt)
    if answer == 'q':
        break
    else:
        print(f"Hello, {answer.title()}!")
        with open(filename, 'a') as file_object:
        	file_object.write(f"{answer.title()}\n")
