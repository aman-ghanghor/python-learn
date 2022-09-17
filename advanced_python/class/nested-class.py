
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name)
        print(self.roll)

    # inner class
    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand)
            print(self.cpu)
            print(self.ram)




stu1 = Student("Rohit", 101)
stu2 = Student("Meera", 102)

stu1.show()
print(stu1.lap.brand)

print()
print()

stu2.show()
print(stu2.lap.brand)
print()


# creating Laptop object outside class
newLap = Student.Laptop()
newLap.show()











