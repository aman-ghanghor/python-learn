# ==========  Reading Data from file  ============
#
#  readline() = This method is used to read single line from a file.
#               Syntax:-  file_object.readline()
#
#  readlines() = This method is used to read all lines from a file.
#                It will return list of line.
#                Syntax:-  file_object.readlines()
#

f = open('student.txt', mode='r')

data1 = f.readline()
data2 = f.readline()

print(data1, end='')
print(data2)

f.close()














