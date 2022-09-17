

class Duck:
    def walk(self):
        print("Thapak Thapak Thapak Thapak")

class Horse:
    def walk(self):
        print("Tagdak Tagdak Tagdak Tagdak")

class Cat:
    def talk(self):
        print("Meow Meow")


def myFun(obj):
    obj.walk()


d = Duck()
h = Horse()
c = Cat()

myFun(d)
myFun(h)
# myFun(c)






