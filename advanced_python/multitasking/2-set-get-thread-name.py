from threading import Thread, current_thread

def disp1():
    print("Child Thread :", current_thread().getName() )
    # print("Child Thread :", current_thread().name)
    current_thread().setName("hello-thread")
    # current_thread().name = "hello-thread"
    print("Child Thread :", current_thread().getName())

def disp2():
    print("Child Thread :", current_thread().getName() )
    current_thread().setName("hii-Thread")
    print("Child Thread :", current_thread().getName())

t1= Thread(target=disp1)
t2 = Thread(target=disp2)

t1.setName("t1-thread")
print(t1.getName())
print(t2.getName())
print()

t1.start()
t2.start()


print("Main Thread :", current_thread().getName())
current_thread().setName("My-Main-Thread")
print("Main Thread :", current_thread().getName())