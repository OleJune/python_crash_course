# Print invitations to guests from the list

guests = ['Monty Python', 'jimmy kimmel', 'AMY Schumer']
guest_1 = guests[0].title()
print(f'Dear, {guest_1}! I am delighted to invite you to dinner this Friday at 7 pm')

guest_2 = guests[1].title()
print(f'Dear, {guest_2}! I am delighted to invite you to dinner this Friday at 7 pm.')

guest_3 = guests[2].title()
print(f'Dear, {guest_3}! I am delighted to invite you to dinner this Friday at 7 pm.')

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

# Remove guests from the list. Print message to each removed person

print('\nI am terribly sorry, but I can invite only two people for dinner.\n')

pop_guest_1 = guests.pop(1)
print(f'Sorry, {pop_guest_1.title()}, due to unforeseen circumstances, the invitation is no longer actuel.')

pop_guest_2 = guests.pop(-1)
print(f'Sorry, {pop_guest_2.title()}, due to unforeseen circumstances, the invitation is no longer actuel.')

pop_guest_3 = guests.pop(-2)
print(f'Sorry, {pop_guest_3.title()}, due to unforeseen circumstances, the invitation is no longer actuel.')

pop_guest_4 = guests.pop(2)
print(f'Sorry, {pop_guest_4.title()}, due to unforeseen circumstances, the invitation is no longer actuel.')

# Inform guests they are still on the list

guest_1 = guests[0].title()
guest_2 = guests[1].title()

print(f'\nDear, {guest_1}! As planned dinner will take place this Friday at 7 pm.')
print(f'Dear, {guest_2}! As planned dinner will take place this Friday at 7 pm.')

# Remove all guests from the list

del guests[0]
del guests[0]
print(guests)
