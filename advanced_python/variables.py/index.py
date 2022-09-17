# ================ TYPE OF VARIABLE =================
#
#  1. Instance Variable
#  2. Class Variable / Static Variables


# - Instance Variable = instance variables are the variables whose separate copy is created in every 
#                       object. 
#                       Instance variables are defined and initialized using a constructor with self
#                       parameter.
#
#
# - Class Variable / Static Variable = class variables are the variables whose single copy is available
#                                      to all the instance of the class.
#
#                                      - If we modify the copy of class variable in an instance, it will
#                                      effect all the copies in the other instance.






class Mobile:
    fp = "Yes"
    def __init__(self, m, p):
        self.model = m          # instance variable
        self.price = p          # instance variable
    
    def show_info(self):
        print("Model :", self.model)
        print("Price :", self.price)

    def set_data(self, m, p):
        self.model = m
        self.price = p

    @classmethod 
    def is_fp(cls):
        print(cls.fp)             # Accessing class/static variable in class method




realMe = Mobile("Real Me", 240)
samsungGalaxy = Mobile("Samsung Galaxy", 400)

# Accessing instance variable
print( realMe.model )
print( realMe.price )
print()


# Accessing class/static variable outside class
print( Mobile.fp )
print()

# Modifying class/static variable
Mobile.fp = "No"
print(Mobile.fp)















