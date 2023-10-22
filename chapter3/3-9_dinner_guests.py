# Print invitations to guests from the list

guests = ['Monty Python', 'jimmy kimmel', 'AMY Schumer']
guest_1 = guests[0].title()
print(f'Dear, {guest_1}! I am delighted to invite you to dinner this Friday at 7 pm.')

guest_2 = guests[1].title()
print(f'Dear, {guest_2}! I am delighted to invite you to dinner this Friday at 7 pm.')

guest_3 = guests[2].title()
print(f'Dear, {guest_3}! I am delighted to invite you to dinner this Friday at 7 pm.')

print('\nThe number of guests invited to dinner are: ' + str(len(guests)))	#working with len() function

# Replace one of the guests who can't make it. Print invitations again

print(f'\nSorry to inform, but {guest_1} cannot make it to dinner.\n')

guests[0] = 'Sacha Baron Cohen'
guest_1 = guests[0].title()

print(f'Dear, {guest_1}! I am delighted to invite you to dinner this Friday at 7 pm.')
print(f'Dear, {guest_2}! I am delighted to invite you to dinner this Friday at 7 pm.')
print(f'Dear, {guest_3}! I am delighted to invite you to dinner this Friday at 7 pm.')

# Add more guests to the list. Print invitations again

print('\nGreat news everybody! I found a bigger dinner table so I can invite more guests.\n')

guests.insert(0, 'aubrey plaza')
guests.insert(2, 'russel peters')
guests.append('Rebel Wilson')

guest_1 = guests[0].title()
guest_2 = guests[1].title()
guest_3 = guests[2].title()
guest_4 = guests[3].title()
guest_5 = guests[4].title()
guest_6 = guests[5].title()

print(f'Dear, {guest_1}! I am delighted to invite you to dinner this Friday at 7 pm.')
print(f'Dear, {guest_2}! I am delighted to invite you to dinner this Friday at 7 pm.')
print(f'Dear, {guest_3}! I am delighted to invite you to dinner this Friday at 7 pm.')
print(f'Dear, {guest_4}! I am delighted to invite you to dinner this Friday at 7 pm.')
print(f'Dear, {guest_5}! I am delighted to invite you to dinner this Friday at 7 pm.')
print(f'Dear, {guest_6}! I am delighted to invite you to dinner this Friday at 7 pm.')

print('\nThe number of guests invited to dinner are: ' + str(len(guests)))	#working with len() function
