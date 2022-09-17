# --------------  RLock ---------------
#
#  A reentrant lock is a synchronization primitive that may be acquired multiple times by the 
#  same thread.
# 
#  The standard Lock doesn't know which thread is currently holding the lock. If the lock is held, 
#  any thread that attempts to acquire it will block, even if the same thread itself is already
#  holding the lock. In such case, RLock(re-entrant Lock) is used.
#
#  A re-entrant lock must be released by the thread that acquired it. Once a thread
#  has acquired a re-entrant lock, the same thread may acquire it again without blocking; 
#  the thread must release it once for each time it has acquired it.


from threading import *

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = RLock()

    def reserve(self, need_seat):
        self.l.acquire()
        print("Available Seats:", self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f"{need_seat} seat is alloted for {name}")
            self.available_seat -= need_seat

        else:
            print("Sorry! All seats has alloted")
        self.l.release()


f = Flight(2)

t1 = Thread(target=f.reserve, args=(1,), name="Rahul")
t2 = Thread(target=f.reserve, args=(1,), name="Sonam")
t3 = Thread(target=f.reserve, args=(1,), name="Meera")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


print("Main Thread")
















