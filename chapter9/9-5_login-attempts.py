class User:
    """A simple attempt to represent a user."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0

user_1 = User('emiko', 'tanaka', 18, 'japan')

print(f"Login attempts by default: {user_1.login_attempts}")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"User's login attempts: {user_1.login_attempts}")

user_1.reset_login_attempts()
print(f"Reset login attempts to default value: {user_1.login_attempts}")

