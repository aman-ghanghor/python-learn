from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def gun(self):
        pass


class AirForce(DefenceForce):
    def area(self):
        print("AirForce class")
        print("Area - Air")
    def gun(self):
        print("Gun - AK-47")

class Army(DefenceForce):
    def area(self):
        print("Army class")
        print("Area - Land")
    def gun(self):
        print("Gun - AK-203")

class Navy(DefenceForce):
    def area(self):
        print("Navy class")
        print("Area - Sea")
    def gun(self):
        print("Gun - M4A1 carbine")




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