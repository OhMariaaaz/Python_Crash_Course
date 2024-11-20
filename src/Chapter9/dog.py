# Note from page

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize the attributes name and age."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

