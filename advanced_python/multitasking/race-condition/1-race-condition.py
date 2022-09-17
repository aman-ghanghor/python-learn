from threading import Thread, current_thread

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
    
    def reserve(self, need_seat):
        print("Available Seats:", self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
        
        else:
            print('Sorry! All seats has alloted')


f = Flight(5)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(5,), name='Sonam')
t1.start()
t2.start()


# Race Condition
#
# Race condition is a situation that occurs when threads are acting in an unexpected sequence, 
# thus leading to unreliable output. This can be eliminated using thread synchronization
#








