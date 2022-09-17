# ------------ Class Method ------------
#
#  - Class Methods are the methods which act upon the class/static variable of the class.
#  
#  - Decorator @classmethod need to write above the class method. 
#
#  - By default, the first parameter of the class methodis cls which refers to the class itself.


class Mobile(object):
    fp = "Yes"
    def __init__(self, m, p):
        self.model = m
        self.price = p

    def get_model(self):
        print(self.model)

    @classmethod
    def show_fp(cls):
        print(cls.fp)


realme = Mobile("RealMe X", 240)

realme.get_model()

Mobile.show_fp()




