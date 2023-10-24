pizzas = ['margherita', 'calzone', 'quattro formaggi']
friend_pizzas = pizzas[:]

pizzas.append('onion pizza')
friend_pizzas.append('marinara')

print('My favourite pizzas are:')
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
