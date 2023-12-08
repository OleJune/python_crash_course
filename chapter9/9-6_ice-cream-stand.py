class Restaurant:
    """Model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
    	"""Initialize name and cuisine attribute."""
    	self.restaurant_name = restaurant_name.title()
    	self.cuisine_type = cuisine_type

    def describe_restaurant(self):
    	"""Display a restaurant's name and it's cuisine."""
    	print(f"The restaurant is called '{self.restaurant_name}'. "
    		f"It specializes in {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Inform that a restaurant is open."""
        print(f"Restaurant '{self.restaurant_name}' is open.")


class IceCreamStand(Restaurant):
	"""Represent an ice cream stand."""
	def __init__(self, restaurant_name, cuisine_type):
	    """
	    Initialize attributes of the parent class.
	    Then initialize attributes specific to an ice cream stand.
	    """
	    super().__init__(restaurant_name, cuisine_type)
	    self.flavors = ['strawberry', 'vanilla', 'caramel']
	    #self.flavors = []

	def display_flavors(self):
		"""Display the flavors of the ice cream."""
		print("\nYou can have an ice cream with the following flavors:")
		for flavor in self.flavors:
		    print(f"--{flavor}")

ice_cream = IceCreamStand('sweet & frozen', 'italian')

ice_cream.display_flavors()

ice_cream.flavors = ['chocolate', 'lemon', 'blueberry']

ice_cream.display_flavors()
