class Restaurant:
    """Model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attribute."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
    	"""Display a restaurant's name and it's cuisine."""
    	print(f"The restaurant is called '{self.restaurant_name}'. "
    		f"It specializes in {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Inform that a restaurant is open."""
        print(f"Restaurant '{self.restaurant_name}' is open.")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, add_number):
        """Increment the number of customers that have been served."""
        self.number_served += add_number

restaurant = Restaurant('fuji', 'japanese')

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 12
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(8)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(62)
print(f"During the day {restaurant.number_served} customers were served.")
