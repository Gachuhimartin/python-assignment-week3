# Base class
class Superhero:
    def __init__(self, name, power, health=100):
        self.name = name
        self.power = power
        self.__health = health   # private attribute (encapsulation)

    def introduce(self):
        return f"I am {self.name}, and my power is {self.power}!"

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            return f"{self.name} has fallen!"
        return f"{self.name} now has {self.__health} health."

    def attack(self):
        return f"{self.name} uses a basic attack!"


# Child class 1 - Polymorphism in action
class Speedster(Superhero):
    def __init__(self, name, power, speed, health=100):
        super().__init__(name, power, health)
        self.speed = speed

    def attack(self):
        return f"{self.name} dashes at lightning speed and strikes with {self.power}!"


# Child class 2
class Strongman(Superhero):
    def __init__(self, name, power, strength, health=100):
        super().__init__(name, power, health)
        self.strength = strength

    def attack(self):
        return f"{self.name} smashes the ground with {self.strength} strength using {self.power}!"


# Example Usage
flash = Speedster("Flash", "Super Speed", speed=999)
hulk = Strongman("Hulk", "Super Strength", strength=1000)

print(flash.introduce())
print(flash.attack())
print(hulk.introduce())
print(hulk.attack())

# Damage demonstration
print(hulk.take_damage(30))
print(hulk.take_damage(80))  # will make him fall
