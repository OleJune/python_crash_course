import json

prompt = "What is your favourite number? "
number = input(prompt)

filename = 'fav_number.json'

with open(filename, 'w') as f:
    json.dump(number, f)
    print(f"{number} is my favourite number too!")
