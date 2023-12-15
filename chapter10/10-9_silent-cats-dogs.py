def show_file_content(filename):
    """Read the text file and print its content to the screen."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
    	pass
    else:
    	print(f"\n{contents.strip()}")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    show_file_content(filename)
