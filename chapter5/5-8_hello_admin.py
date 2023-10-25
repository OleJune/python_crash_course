# Loop through the list, and print a greeting to each user

users = ['evan', 'jane', 'admin', 'HELEN', 'anne']

for user in users:
	if user == 'admin':
		print(f'Hello, {user}! Would you like to see a status report?')
	else:
		print(f'Hello, {user.title()}!')
