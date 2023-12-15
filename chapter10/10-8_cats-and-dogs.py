def show_file_content(filename):
    """Read the text file and print its content to the screen."""
    with open(filename) as f:
        contents = f.read()
    print(f"\n{contents.strip()}")

#show_file_content('cats.txt')

#filenames = ['cats.txt', 'dogs.txt']
#for filename in filenames:
#    show_file_content(filename)


# Wrap the code in a try-except block
def show_file_content(filename):
    """Read the text file and print its content to the screen."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
    	print(f"\nThe file {filename} does not exist.")
    else:
    	print(f"\n{contents.strip()}")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    show_file_content(filename)
