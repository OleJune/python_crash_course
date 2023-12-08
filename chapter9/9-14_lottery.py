from random import choice

lottery_tickets = ['a', 'd', 'g', 'q', 'r', 3, 13, 23, 33, 9, 19, 29, 39, 5, 55]
lucky_numbers = []

for i in range(4):
    winner = choice(lottery_tickets)
    lucky_numbers.append(winner)
    lottery_tickets.remove(winner)

print(f"\nAny ticket matching next 4 numbers or letters"
      f" wins the prize: {lucky_numbers}")

# OR

lottery = [8, 18, 28, 35, 6, 16, 26, 36, 90, 51]
winning_ticket = []

while len(winning_ticket) < 4:
    number = choice(lottery)
    if number not in winning_ticket:
        winning_ticket.append(number)

print(f"\nAny ticket matching next 4 numbers or letters"
      f" wins the prize: {winning_ticket}")
