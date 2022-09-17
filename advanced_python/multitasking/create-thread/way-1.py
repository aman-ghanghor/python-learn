#  Thread class of threading module is used to create threads. To create our own thread we need to 
#  create an object of Thread Class.
#
#  Following are the ways of creating threads:-
#
#  1. Creating a thread without using a class.
#  2. Creating a thread by creating a child class to Thread class.
#  3. Creating a thread without creating child class to Thread class


#  -----  -----  ----- Create thread Without creating any class -----  -----

from threading import Thread

def disp(a, b):
    print("Thread Running", a, b)
    for i in range(5):
        print("Child Thread")

t = Thread(target=disp, args=(10, 20))    # create a thread by making object of Thread class
t.start()       # Start thread


for i in range(5):
    print("Main Thread")
