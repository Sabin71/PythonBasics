class Restaurant:
    """A simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Add attribute with default value

    def describe_restaurant(self):
        """Display a description of the restaurant."""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def set_number_served(self, number_served):
        """Set the number of customers served."""
        self.number_served = number_served

    def increment_number_served(self, customers):
        """Increment the number of customers served by a given amount."""
        self.number_served += customers

    def display_number_served(self):
        """Display the number of customers served."""
        print(f"Number of customers served: {self.number_served}")

class User:
    """A simple user class."""

    def __init__(self, first_name, last_name):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0  # Add attribute for login attempts

    def describe_user(self):
        """Display a description of the user."""
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0

# Restaurant Example
restaurant = Restaurant("PHO", "Thai")
restaurant.describe_restaurant()
print(f"Initial number of customers served: {restaurant.number_served}")

# Change the number of customers served
restaurant.set_number_served(320)
print(f"Number of customers served after setting: {restaurant.number_served}")

# Increment the number of customers served
restaurant.increment_number_served(320)

print(f"Number of customers served after increment: {restaurant.number_served}")

# User Example
user = User("Sarah", "Benn")
user.describe_user()

# Increment login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Number of login attempts: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()
print(f"Number of login attempts after reset: {user.login_attempts}")

