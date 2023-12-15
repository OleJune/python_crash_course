import json

filename = 'favourite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favourite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"Your favourite number is {number}.")
