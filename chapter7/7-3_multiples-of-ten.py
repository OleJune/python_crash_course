prompt = input("Enter a number, and I will tell you if it is a multiple of 10 or not: ")
number = int(prompt)

if number % 10 == 0:
	print(f"\nNumber {number} is a multiple of 10.")
else:
	print(f"\nNumber {number} is not a multiple of 10.")
