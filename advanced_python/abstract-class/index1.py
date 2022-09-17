from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print("AK-47")

class AirForce(DefenceForce):
    def area(self):
        print("AirForce class")
        print("Area - Air")

class Army(DefenceForce):
    def area(self):
        print("Army class")
        print("Area - Land")

class Navy(DefenceForce):
    def area(self):
        print("Navy class")
        print("Area - Sea")


af = AirForce()
af.gun()
af.area()
print()

ar = Army()
ar.gun()
ar.area()
print()

nv = Navy()
nv.gun()
nv.area()
print()