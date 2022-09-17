# ===========  Reading Data from file  ==========
#
#  read(size) = This method is used to read data/content from a file and returns it as string
#               in text mode or bytes object in binary mode

#               Syntax:-  file_object.read(size)     
#
#             - Where size represents the number of bytes to be read from the beginning of the 
#               file
#              
#             - When size is omitted or negative, the entire contents of the file will be read
#               and returned
#
#             - If the end of the file has been reached, file_object.read() will return an 
#               empty string ('')

import os

f = open('student.txt', mode='r')

if(os.path.isfile('student.txt') and f.readable()):
    # data = f.read()
    data1 = f.read(8)   # first 8 character
    data2 = f.read(2)   # next 2 character
    print(data1)
    print(data2)
else:
    print("Unable to read!!!")

f.close()