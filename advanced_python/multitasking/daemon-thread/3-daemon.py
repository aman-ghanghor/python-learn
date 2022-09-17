# ----- ====== ------- ------- ====== -------
#  *  Main Thread is always non-daemon thread.
#
#  *  Rest of the threads inherits daemon nature from thier parents.
#  *  If parent thread is non daemon then child thread will become non-daemon thread.
#  *  If parent thread is daemon then child thread will also become a daemon thread.
#  
#  *  When last non-daemon thread terminates, automatically all daemon threads will 
#     be terminated. We are not required to terminate daemon thread explicity


from threading import Thread, current_thread
from time import sleep

def teacher():
    for i in range(1, 11):
        print("Teaching Session", i)
        sleep(1)

t1 = Thread(target=teacher)
t1.setDaemon(True)
t1.start()
sleep(6)
print("Exam Finished", current_thread().name)

























