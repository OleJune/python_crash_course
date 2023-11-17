def make_shirt(text_printed='i love python', size='large'):
	"""Summerize the size of the shirt and the message printed on it."""
	print(f"\nThe size of the t-shirt is {size}.")
	print(f"The message printed on it says: '{text_printed.upper()}'.")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text_printed='monty python')
make_shirt('wild, wild python', 'small')
