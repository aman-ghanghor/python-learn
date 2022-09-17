
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def disp(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)


class User:
    @staticmethod
    def show(s):
        print("User Name:", s.name)
        print("User Roll:", s.roll)


stu = Student("Rahul", 101)

stu.disp()
print()

User.show(stu)