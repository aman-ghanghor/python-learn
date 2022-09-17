# ----------- Instance Method -----------
#
#   - Instance methods are the methods which act upon the instance variables of the class.
#   - Instance method need to know the memory address of the instance which is provided 
#     through self variable by default as first parameter for the instance method.
#
#   - We can categorized instance method :
#       
#           (i)   Accessor method
#           (ii)  Mutator method


class Mobile:
    def __init__(self):
        self.model = "Realme X"

    def get_model(self):
        return self.model

    def set_model(self, m):
        self.model = m


realme = Mobile()

print(realme.get_model())

realme.set_model("Realme Pro")

print(realme.get_model())




















