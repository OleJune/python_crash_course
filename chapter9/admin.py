"""Set of classes used to represent a user."""

from only_user import User

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

    def change_privileges(self, privileges=[]):
        """Set a new list of the privileges the admin has."""
        self.privileges = privileges

class Admin(User):
    """Represent an administrator."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
