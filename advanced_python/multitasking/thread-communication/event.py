# ---------------- Event ----------------
#
#  This is one of the simplest mechanisms for communication between threads:
#  one thread signals an event and other threads wait for it.
# 
#  An event object manages an internal flag that can be set to true with the set()
#  method and reset to false with the clear() method. The wait() method blocks 
#  until the flag is true.
#
#  The flag is initially False.


# =========  Create Event Object  ==========
#
#   from threading import Event
#   e = Event()



# =========  Event Method  ==========
#
#   set() =  It sets the internal flag to true. All threads waiting for it to become true
#            are awakened. Threads that call wait() once the flag is true will not block at all.
#
#   clear() = It resets the internal flag to false. Subsequently, threads calling wait() will
#             block until set() is called to set the internal flag to true again.
#
#   is_set() = It return true if and only if the internal flag if true.
#
#
#
#   wait(timeout=None) = It blocks until the internal flag is true. If the internal flag is true
#                        on entry, return immediately. Otherwise, block until another thread calls
#                        set() to set the flag to true, or until the optional timeout occurs.
#
#                       - When the timeout argument is present and not None, it should be a floating point
#                         number specifying a timeout for the operation in seconds (or fractions thereof).
#
#                       - This method returns true if and only if the internal flag has been set to true, 
#                         either before that wait call or after the wait starts, so it will always return 
#                         True except if a timeout is given and the operation  times out.
#


from threading import Thread, Event
from time import sleep

def light_switch():
    sleep(3)
    e.set()
    print("Green Light ON")
    sleep(5)
    print("Red Light ON")
    e.clear()


def traffic():
    e.wait()
    while e.is_set():
        print("You can Go........")
        sleep(0.5)
    print("Program Done")
    
    
e = Event()
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)

t1.start()
t2.start()
















































