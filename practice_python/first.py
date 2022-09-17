
class Computer(object):
    os = 'window'   # class variable OR static variable

    def __init__(self, ram, cpu, storage, keyboard_brand, keyboard_total_keys):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
        # self.keyboard = self.Keyboard(keyboard_brand, keyboard_total_keys)

    def showInfo(self):
        print(f'RAM = {self.ram} | CPU = {self.cpu} | STORAGE = {self.storage}')

    def setRAM(self, r):
        self.ram = r 
    
    # class method
    @classmethod
    def getOS(cls):
        return cls.os
    
    @classmethod
    def setOS(cls, newos):
        cls.os = newos

    @staticmethod
    def gbToBytes(gb):
        return gb*1024*1024*1024


    # NESTED CLASS
    class Keyboard:
        isMachanical = 'NO'
        
        def __init__(self, brand, total_keys):
            self.brand = brand
            self.totalKeys = total_keys

        def showInfo(self):
            print(f'BRAND = {self.brand}, TOTAL_KEYS = {self.totalKeys}')


mypc = Computer('4 GB', 'Intel i7', '1 TB', 'Logitech', '105')

mypc.showInfo()

mypc.Keyboard('Logitech', 105).showInfo()




















