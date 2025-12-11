#Khalid Althomali 
#OOP Practice

# Parent class
# Encabsulation and Abstraction 
class Vehicle:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this")

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self):   # <-- FIXED
        self.brand = "Toyota"
        self.model = "Camry"
# Polymorphism
    def sound(self):
        return "Vroom!"


# Test
car = Car()
print(car.brand, car.model)   # Toyota Camry
print(car.sound())            # Vroom!



