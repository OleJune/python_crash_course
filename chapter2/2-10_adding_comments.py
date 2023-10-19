# Print a quote of a famous person

quote = '"Ukraine begins with you."'
message = 'Vyacheslav Chornovil once said, ' + quote	# Compose a message using string concatenation
print(message)


quote = '"Ukraine begins with you."'
message = f'Vyacheslav Chornovil once said, {quote}'	# Compose a message using f-string
print(message)

# Print the message using stripping function strip()

pet_names = '\tMy lovely pets: Ginger the Cat and Blacky.\t\n'
print(pet_names)
pet_names = pet_names.strip()
print(pet_names)