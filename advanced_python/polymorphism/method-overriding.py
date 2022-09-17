# Method Overriding

class Add:
    def result(self, a, b):
        print("Addition :", a + b)


class Multi(Add):
    def result(self, a, b):
        super().result(a,b)
        print("Multiplication :", a*b)



m = Multi()

m.result(10, 20)