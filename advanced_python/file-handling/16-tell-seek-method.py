# ============ Methods ============
#
#  tell() = This method is used to find current position of file pointer from 
#           beginning of the the file. Position starts from 0.
#           Syntax:-  file_object.tell()
#
#
#


f = open('student.txt', mode='r')

pos1 = f.tell()
print(pos1)

print(f.read(5))

pos2 = f.tell()
print(pos2)

print(f.read(3))

pos3 = f.tell()
print(pos3)

f.close()

