
# Activity 1: Create a class with attributes, methods, constructors, and inheritance

# Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.__battery_life = battery_life   # Encapsulation: private attribute

    def get_battery_life(self):
        return self.__battery_life

    def set_battery_life(self, hours):
        if hours > 0:
            self.__battery_life = hours

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

# Child class inheriting from Smartphone
class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a {self.camera_megapixels}MP photo with {self.brand} {self.model}!")


# Example usage
phone1 = SmartPhoneWithCamera("Samsung", "Galaxy S23", 24, 108)
phone1.call("+123456789")
phone1.take_photo()
print("Battery life:", phone1.get_battery_life(), "hours")


# Activity 2: Polymorphism Challenge 🎭

class Animal:
    def move(self):
        pass  # Placeholder method to be overridden

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# Example usage of polymorphism
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    animal.move()
