# ============ Methods ============
#
#  tell() = This method is used to find current position of file pointer from 
#           beginning of the the file. Position starts from 0.
#           Syntax:-  file_object.tell()
#
#  seek(position) = This method is used to move file pointer from one position to
#                   another position from beginning of the file. Position starts
#                   from 0 and it must be positive integer.
#                   Syntax:-  file_object.seek(position)

f = open('student.txt', mode='r')

f.seek(5)
print(f.tell())

print(f.read(4))

f.close()





