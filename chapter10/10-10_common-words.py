def count_words(filename, text):
    """Count the approximate number of specific words or phrases in a file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
    	pass
    else:
        number = contents.lower().count(text)
        if number == 1:
            print(f"\n<{text.upper().strip()}> appears approximately once"
                f" in {filename}.")
        elif number > 1: 
            print(f"\n<{text.upper().strip()}> appears approximately"
                f" {number} times in {filename}.")
        elif number == 0:
            print(f"\nThere is no <{text.upper().strip()}> in {filename}.")

count_words('oliver_twist.txt', 'tomorrow')

count_words('the_odyssey.txt', 'maybe')

count_words('oliver_twist.txt', 'the')  # Very approximate count.

filenames = ['oliver_twist.txt', 'the_odyssey.txt']

for filename in filenames:
	count_words(filename, 'the ')  # More precise count using space in the end.
