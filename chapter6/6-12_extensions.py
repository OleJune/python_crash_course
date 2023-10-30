# Extend this example program:

#user = {
#	'username' : 'riser',
#	'first' : 'rina',
#	'last' : 'serano',
#	}
#for key, value in user.items():
#	print(f'\nKey: {key}')
#	print(f'Value: {value}')

print('# Make a list of dictionaries, loop through it and print all the info:')

users = []

user = {
	'username' : 'riser',
	'first' : 'rina',
	'last' : 'serano',
	}
users.append(user)

user = {
	'username' : 'maryjane',
	'first' : 'mary',
	'last' : 'jane',
	}
users.append(user)

user = {
	'username' : 'ricko',
	'first' : 'rick',
	'last' : 'owens',
	}
users.append(user)

for user in users:
	print(f"\nUser's info:")
	for key, info in user.items():
		print(f"--{key}: {info.title()}")

print("\n# Add new key-value pairs to all dictionaries "
	"and modify values just in one of them.")
print("\n# Make output more neat using title() method.")

for user in users:
	user['status'] = 'active'      # add two new key-value pairs 
	user['gender'] = 'female'
	user['username'] = user['first'] + user['last']  # modify an existing key-value pair
	if user['first'] == 'rick':   # modify values in one of the dictionaries
		user['gender'] = 'male'
		user['status'] = 'banned'
	print(f"\nUser's info:")
	for key, info in user.items():
		if key == 'status':
			print(f"--{key}: {info}")
		elif key == 'gender':
			print(f"--{key}: {info}")
		else:
			print(f"--{key}: {info.title()}")

print('\n# Remove one key-value pair and print modified data:')

for user in users:
    del user['gender']       # remove one key-value pair
    print(f"\nUser's info:")
    for key, info in user.items():
	    if key == 'status':
	        print(f"--{key}: {info}")
	    else:
		    print(f"--{key}: {info.title()}")

print('\n# Print a personalized message to the banned user:')
#if user['status'] == 'banned':
#	print(f"\n{user['username']}, you are no longer a member of this community.")
#	username = user['username'].title()
#	print(f"\n{username}, we cancelled your membership.")

#for user in users:
#	username = user['username'].title()
#	print(username)

for user in users:
	username = user['username'].title()
	if user['status'] == 'banned':
		print(f"\n{username}, we cancelled your membership. "
			f"You are no longer a member of this community.")
	else:
		print(f"\nHi {username}, how can we help you?")

print('\n# Check the status of each user:')

for user in users:
	print("\nUser's current status is:")
	for key, status in user.items():
		if key == 'status':
			print(f'{status}')

print('\n# Improve the formatting of the output:')

for user in users:
	username = user['username'].title()
	print(f"\n{username}'s current status is:")
	for key, status in user.items():
		if key == 'status':
			print(f'\t<{status}>')
