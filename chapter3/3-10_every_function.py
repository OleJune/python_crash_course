#  Creat an empty list

nz_endemics = []
print(nz_endemics)

# Add items to the list

nz_endemics.append('kiwi')
nz_endemics.append('tomtit')
nz_endemics.append('kākāpō')
nz_endemics.append('takahē')
nz_endemics.append('ruru')

print(f'List of endemic birds of New Zealand:\n{nz_endemics}.')

# Add more birds to the list

nz_endemics.insert(1, 'weka')
nz_endemics.insert(3, 'rook')

print(f'\nTwo more endemics added to the list:\n{nz_endemics}.')

# Delete item with del statement

print(f'\nRook is not endemic. It was brought to NZ from England.')
del nz_endemics[3]
print(nz_endemics)

# Delete item with pop() method

native = nz_endemics.pop()
print(f'\n{native.title()} nests in other countries too. It is native but not endemic.')
print(nz_endemics)

# Add a bird to the list

print('\nAre there other endemic birds in NZ?')
print(f'Sure, there are 92 endemics in NZ. One of them is fantail.')
nz_endemics.append('fantail')
print(nz_endemics)

# Delete item with remove() method

print("\nSorry, but isn't fantail breeds in Australia as well?")
removed_bird = 'fantail'
nz_endemics.remove(removed_bird)
print(f'You are right. {removed_bird.title()} is native.')
print(nz_endemics)

# Sort the list with reverse() method

print('\nIn reverse order:')
nz_endemics.reverse()
print(nz_endemics)

# Sort the list with sorted() function

print('\nIn alphabetical order using SORTED():')
print(sorted(nz_endemics))

print('\nIn reverse alphabetical order:')
print(sorted(nz_endemics, reverse=True))

print('\nIn original order:')
print(nz_endemics)

# Sort the list with sort() method

print('\nIn alphabetical order using SORT():')
nz_endemics.sort()
print(nz_endemics)

print('\nIn original order:')
print(nz_endemics)

print('\nIn reverse alphabetical order:')
nz_endemics.sort(reverse=True)
print(nz_endemics)

# Count the number of birds in the list

print(f'\nThere are ' + str(len(nz_endemics)) + ' birds in the final list.')

