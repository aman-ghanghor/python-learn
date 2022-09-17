#  sleep() Method is used to stop execution of a program temporarily for a given amount of time.
#  When this function is called, PVM stops program execution for given amount of time.
#  It belongs to the time module.

import time

for i in range(20):
    print(i)
    if i==10:
        time.sleep(5)