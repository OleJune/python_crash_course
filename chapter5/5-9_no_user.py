# Check if the list of users is not empty

#users = ['evan', 'jane', 'admin', 'helen', 'anne']
users = []

if users:
	for user in users:
	    if user == 'admin':
		    print(f'Hello, {user}! Would you like to see a status report?')
	    else:
		    print(f'Hello, {user.title()}!')
else:
    print('We need to find some users!')
