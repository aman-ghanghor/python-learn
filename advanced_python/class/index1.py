
class Mobile:
    def __init__(self, m, p=150):
        self.model = m
        self.price = p
        print("id of self:", id(self))

    def show_info(self):
        print(self.model)
        print(self.price)

    def set_data(self, m, p):
        self.model = m
        self.price = p



m1 = Mobile("Samsung Galaxy")
print("m1:", id(m1))
print()

print(m1.show_info())
print()

m1.set_data("Real Me", 240)
print(m1.show_info())












