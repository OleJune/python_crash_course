# Print invitations to guests from the list

guests = ['Monty Python', 'jimmy kimmel', 'AMY Schumer']
guest_1 = guests[0].title()
print(f'Dear, {guest_1}! I am delighted to invite you to dinner this Friday at 7 pm.')

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
