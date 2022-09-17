class Mobile(object):
    def __init__(self, m, p):
        self.model = m
        self.price = p
        print("id of self:", id(self))
    
    def show(self):
        print("model:", self.model)
        print("price:", self.price)

    def setModel(self, m, p):
        self.model = m
        self.price = p

mobileObj = Mobile("Samsung galaxy", 160)
print("id of mobileObj:", id(mobileObj))
print()

# Calling method
print(mobileObj.show())
print()

# Set Model and price
mobileObj.setModel("Realme X", 200)

print(mobileObj.show())
print()

# Accessing property
print("model:", mobileObj.model)




















