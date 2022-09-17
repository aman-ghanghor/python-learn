class Mobile:
    fp = "Yes"
    def __init__(self, m, p):
        self.model = m
        self.price = p 

    # without parameter
    @staticmethod
    def show_model():
        print(Mobile.fp)

    # with parameter
    @staticmethod
    def show_info(m, p):
        model = m
        price = p 
        print(model, price)




obj = Mobile("RealMe X", 120)

Mobile.show_model()

print("")

Mobile.show_info("Samsung Galaxy", 248)

