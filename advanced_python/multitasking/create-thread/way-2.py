# ---  ---  Creating a thread by creating child class to thread class ---  ---
#
#  start() = start/run thread
#  
#  run() = Every thread will run this method when thread is started. We can override this method
#          and write our own code as body of the method. A thread will terminate automatically 
#          when it comes out of the run() Method.
#
#  join() = This method is used to wait till the thread completely executes the run() method
#
#


from concurrent.futures import thread
from threading import Thread


# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("Child Thread: ", i)

# thread_object = MyThread()
# # print(thread_object.name)
# print(thread_object.getName())
# thread_object.start()
# thread_object.join()

# for i in range(5):
#     print("Main Thread")






# --------- Thread Child Class with Constructor -------

class MyThread(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        self.count = a 
        print("Child Thread Constructor")
    
    def run(self):
        for i in range(self.count):
            print("Child thread -", i)


thread_obj = MyThread(5)
thread_obj.start()
print("Main Thread")



















