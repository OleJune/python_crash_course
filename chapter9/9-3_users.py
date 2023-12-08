class User:
    """A simple attempt to represent a user."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()

    def describe_user(self):
        """Summarize the information about a user."""
        print("\nHere is all the information about a user:")
        print(f"\tName: {self.first_name}"
            f"\n\tLast name: {self.last_name}"
            f"\n\tAge: {self.age}"
            f"\n\tLocation: {self.location}")

    def greet_user(self):
        """Print a greeting to a user."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nHello, {full_name}!")
    
user_0 = User('nadine', 'arno', 24, 'france')

user_1 = User('jack', 'gordon', 35, 'england')

user_2 = User('emiko', 'tanaka', 18, 'japan')

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
