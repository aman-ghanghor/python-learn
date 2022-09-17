
class Father:
    def __init__(self):
        self.money = 5000
        print("Father class constructor")
    def showF(self):
        print("Father class method")


class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class constructor")
    def showS(self):
        print("Son class method")


class Daughter(Father):
    def __init__(self, m):
        super().__init__()
        self.money = m
        print("Daughter class constructor")
    def showD(self):
        print("Daughter class method")



s1 = Son()
d1 = Daughter(8000)
print()

s1.showS()
s1.showF()
print(s1.money)
print()

d1.showD()
d1.showF()
print(d1.money)







