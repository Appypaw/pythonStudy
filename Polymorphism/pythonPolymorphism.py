class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Airplane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Genesis", "G80")
boat1 = Boat("STX", "OilRig")
airplane1 = Airplane("Boeing", "787")

for x in (car1, boat1, airplane1):
    x.move()

#다형성때문에 다른 클래스들의 같은 메소드를 반복문으로 실행시킬 수 있음.