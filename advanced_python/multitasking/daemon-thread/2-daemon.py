# ----- ====== ------- ------- ====== -------
#  *  Main Thread is always non-daemon thread.
#
#  *  Rest of the threads inherits daemon nature from thier parents.
#  *  If parent thread is non daemon then child thread will become non-daemon thread.
#  *  If parent thread is daemon then child thread will also become a daemon thread.
#  
#  *  When last non-daemon thread terminates, automatically all daemon threads will 
#     be terminated. We are not required to terminate daemon thread explicity.


from threading import Thread, current_thread

def disp():
    print("Disp Function")
    T2 = Thread(target=show)
    print("T2 child of T1 isDaemon:", T2.isDaemon())

def show():
    print("Show Function")



print("MainThread isDaemon:", current_thread().daemon )

t1 = Thread(target=disp)
print("T1 isDaemon (Before):", t1.isDaemon())
t1.setDaemon(True)
print("T1 isDaemon (After):", t1.isDaemon())

t1.start()
t1.join()

print("Main Thread")























