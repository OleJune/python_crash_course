from random import randint

class Die:
    """Model a die."""
    def __init__(self, sides=6):
        """Initialize attributes."""
        self.sides = sides
    
    def roll_die(self):
        """Roll a die 10 times and print the result."""
        print(f"\nRoll {self.sides}-sided die 10 times. Show the results.")
        for roll in range(10):
        	print(randint(1, self.sides))

die_6 = Die()
die_6.roll_die()

die_10 = Die(10)
die_10.roll_die()

die_20 = Die(20)
die_20.roll_die()
