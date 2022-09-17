#  ----  ----  Creating a thread without creating a child class to Thread class  ----  ----
#
#  We can create an independent thread child class that does not inherit from Thread Class

from threading import Thread

class MyThread:
    def disp(self, a, b):
        print(a, b)

mythread = MyThread()

t = Thread(target=mythread.disp, args=(10, 20))
t.start()




 








