
class MyClass:
    def sum(self, a=None, b=None, c=None):
        if(a!=None and b!=None and c!=None):
            result = a + b + c
        elif(a!=None and b!=None):
            result = a + b
        else:
            result = "Provide atleast two number!!!"
        print(result)
            
           
            
obj = MyClass()

obj.sum(10, 20, 30)

obj.sum(10, 20)

obj.sum(10)