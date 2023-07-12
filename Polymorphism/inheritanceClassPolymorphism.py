class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Airplane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Genesis", "G90")
boat1 = Boat("Ibiza", "Touring 20")
airplane1 = Airplane("Boeing", "747")

for x in (car1, boat1, airplane1):
    print(x.brand)
    print(x.model)
    x.move()

"""
Genesis
G90
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!
"""

