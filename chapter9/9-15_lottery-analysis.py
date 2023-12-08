from random import choice

def generate_ticket(lottery=[], ticket=[]):
    """Create a lottery ticket containing 4 random numbers or letters."""
    while len(ticket) < 4:
        number = choice(lottery)
        if number not in ticket:
            ticket.append(number)
    return ticket

def compare_tickets(any_ticket=[], winning_ticket=[]):
    """Check if a ticket matches a winning ticket."""
    if winning_ticket == any_ticket:
    	print("\nCongrats! You've won a lottery!") 
    else:
    	print("\nThis ticket doesn't match a winning ticket. "
		    "Try another ticket!")

def loop_runs(loop):
    """Report how many times the loop had to run to win a lottery."""
    if loop == 0:
        print("\nIt's your lucky day!")
    elif loop == 1:
        print(f"\nIt only took {loop} loop to get a winning ticket!")
    else:
        print(f"\n{loop} loops later your ticket finally matches a winning ticket!")

lottery_tickets = ['a', 'd', 'g', 'q', 'r', 3, 13, 23, 33, 9, 19, 29, 39, 5, 55]
lucky_ticket = []
my_ticket = []

lucky_t = generate_ticket(lottery_tickets, lucky_ticket)
print(f"\nAny ticket matching next 4 numbers or letters "
	f"wins the prize: {lucky_t}")

my_t = generate_ticket(lottery_tickets, my_ticket)
print(f"\nMy first ticket: {my_t}")

compare_tickets(my_ticket, lucky_ticket)

loops = 0

while True:
    if lucky_ticket == my_ticket:
        print(f"\nYour new ticket: {my_ticket}. "
        f"You've won a lottery!")
        break
    elif lucky_ticket != my_ticket:
        for i in range(4):
            del my_ticket[0]
        generate_ticket(lottery_tickets, my_ticket)
        loops += 1

loop_runs(loops)
