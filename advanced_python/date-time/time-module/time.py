from time import time, ctime, localtime

epoch =  time()
print(epoch)
print()

et = ctime(epoch)
print(et)
print()

print(ctime())
print()

stobj = localtime()            # return struct_time object
print(stobj)
print(stobj.tm_mday, end="-")
print(stobj.tm_mon, end="-")
print(stobj.tm_year)












