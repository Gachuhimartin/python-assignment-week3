# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        # generic placeholder
        print(f"{self.name} is moving...")

# Child classes
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing 🚤")

class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is pedaling 🚴")

# Example usage
vehicles = [
    Car("Toyota"),
    Plane("Boeing 747"),
    Boat("Titanic"),
    Bicycle("Mountain Bike")
]

# Polymorphism in action
for v in vehicles:
    v.move()
