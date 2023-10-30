favourite_languages = {
	'jen' : 'python',
	'sam' : 'c',
	'iren' : 'ruby',
	'phil' : 'python',
    }

# Make a list of people who should take a poll.
# Print different messages to those who've taken the poll and to those who haven't.

people_poll = ['jack','sam', 'oggi', 'iren']

for name in people_poll:
	if name in favourite_languages.keys():
		print(f'\nThank you for your respond, {name.title()}.')
	else:
		print(f'\nHi {name.title()}, please take the poll.')
