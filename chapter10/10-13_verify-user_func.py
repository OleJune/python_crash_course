import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new user."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username 

def verify_user():
    """Prompt for verification."""
    username = get_stored_username()
    verify = input(f"{username.title()} is that you? (y / n) ")
    if verify == 'y':
        return username
    else:
        new_user = get_new_username()
        return new_user

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username: 
        user = verify_user()
        print(f"Welcome back, {user.title()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}!")
        
greet_user()