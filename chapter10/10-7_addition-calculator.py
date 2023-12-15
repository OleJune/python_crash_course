print("\nEnter two numbers and I'll add them. "
	"(enter 'q' to quit)")

while True:
	first_n = input("\nEnter first number: ")
	if first_n == 'q':
		break
	second_n = input("Enter second number: ")
	if second_n == 'q':
		break
	try:
		result = int(first_n) + int(second_n)
	except ValueError:
		print("Please, enter an integer!")
	else:
		print(f"Result: {result}")
