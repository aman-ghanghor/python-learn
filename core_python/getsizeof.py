# --------- getsizeof() Function ----------
# 
#  This function returns the size of an object in bytes.
#  The object can be any type of object
#  All built-in objects will return correct results, but this does not have to hold true for
#  third-party extensions as it is implementation specific
# 
#  Only the memory consumption directly attributed to the object is accounted for, not the 
#  memory consumption of objects it refers to.
#
#  This is part of sys module so you have to import sys module before using this function.
#
#  Syntax:-
#             from sys import *
#             getsizeof(object)


from sys import getsizeof


myList = [10, 20, 30, 40]

print(getsizeof(myList))
