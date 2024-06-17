#Observer pattern
class Customer:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} has been notified about the ice cream stock.")
