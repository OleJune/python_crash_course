def make_shirt(size, text_printed):
	"""Summerize the size of the shirt and the message printed on it."""
	print(f"\nThe size of the t-shirt is {size}.")
	print(f"The message printed on it says: '{text_printed.upper()}'.")

make_shirt(6, 'proud ukrainian')
make_shirt(text_printed='proud ukrainian', size=10)
