class Father:
    def __init__(self, money):
        self.money = money
        print("Father Constructor")
    def showF(self):
        print("Father class method")


class Son(Father):
    def __init__(self, money):
        super().__init__(money)
        print("Son Constructor")
    def showS(self):
        print("Son class method")


class GrandSon(Son):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job
        print("GrandSon Constructor")
    def showG(self):
        print("Son class method", self.money, self.job)


gs1 = GrandSon(4000, "Peon")
print()
gs1.showG()
gs1.showS()
gs1.showF()