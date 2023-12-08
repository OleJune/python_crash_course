class Restaurant:
    """Model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
    	"""Initialize name and cuisine attribute."""
    	self.restaurant_name = restaurant_name
    	self.cuisine_type = cuisine_type

    def describe_restaurant(self):
    	"""Display a restaurant's name and it's cuisine."""
    	print(f"The restaurant is called '{self.restaurant_name.title()}'. "
    		f"It specializes in {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Inform that a restaurant is open."""
        print(f"Restaurant '{self.restaurant_name.title()}' is open.")

restaurant = Restaurant('fuji', 'japanese')
my_favourite_restaurant= Restaurant('promin', 'european')
restaurant_to_visit = Restaurant('dioscuri', 'georgian')

restaurant.describe_restaurant()

my_favourite_restaurant.describe_restaurant()

restaurant_to_visit.describe_restaurant()
