"""Set of classes used to represent a user."""

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

class Privileges:
    """Represent admin's privileges."""
    def __init__(self, privileges=[]):
        """Initialize attributes."""
        self.privileges = [
        'can add post', 'can delete post', 'can ban user',
        'can edit post'
        ]

    def show_privileges(self):
        """Display the privileges the admin has."""
        print(f"\nThis user is an admin. They have next privileges:")
        for privilege in self.privileges:
            print(f"--{privilege}")


class Admin(User):
    """Represent an administrator."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
