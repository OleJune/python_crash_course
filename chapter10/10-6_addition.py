print("\nEnter two numbers and I'll add them together. "
	"(enter 'q' to quit)")

first = input("\nEnter first number: ")
second = input("Enter second number: ")

try:
	result = int(first) + int(second)
except ValueError:
	print("You provided text instead of a number!")
else:
	print(f"Result: {result}")
