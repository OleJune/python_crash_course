# Make sure a new username is unique

current_users = ['evan', 'jane', 'admin', 'helen', 'anne']

new_users = ['kara', 'nate', 'ANNE', 'amie', 'Jane']

for new_user in new_users:
	if new_user.lower() in current_users:
		print('Please, create a new username.')
	else:
		print(f'Username "{new_user}" is available.')
