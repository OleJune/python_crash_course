"""A class used to represent a user."""

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
