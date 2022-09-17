
# ------------- parent class*+ ------------
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Parent Class Constructor")



# ------------- child class
class Student(Human):
    def __init__(self, name, age, roll, school):
        super().__init__(name, age)
        self.roll = roll
        self.school = school
        print("Child class constructor")

    def show(self):
        print("name :", self.name)
        print("age :", self.age)
        print("roll :", self.roll)
        print("school :", self.school)



stu1 = Student("Rahul", 13, 101, "Delhi Public School")
print()
stu1.show()











