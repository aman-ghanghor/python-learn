
class Father:
    def __init__(self):
        super().__init__()
        print("Father class constructor")
    def showF(self):
        print("Father class method")


class Mother:
    def __init__(self):
        super().__init__()
        print("Mother class constructor")
    def showM(self):
        print("Mother class method")

    
class Son(Father, Mother):
    def __init__(self):
        super().__init__()                 # Calling parent class constructor
        print("Son class constructor")
    def showS(self):
        print("Son class method")



s = Son()
print()

s.showS()
s.showF()
s.showM()




































