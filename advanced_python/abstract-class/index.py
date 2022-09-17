from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("Concrete method")


class Child(Father):
    # defining abstract method
    def disp(self):
        print("Child class")
        print("Defining Abstract method")


c = Child()
c.disp()
c.show()


