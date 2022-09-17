# =========== Writing Data to the file ===========
#
#   write() = This method is used to store/write character or string into the file
#             represented by the file object. It returns the number of character written.
#             Syntax:-  file_object.write(string)             
#
#   writelines() = This method is used to store/write group of string (list, tuple, set) into
#                  the file represented by the file object.
#                  Syntax:-  file_object.writelines(group of string)
#

f = open('student.txt', mode='w')

lst = ['Rahul\n', 'Sonam\n', 'Radha\n', 'Meera\n']
f.writelines(lst)

f.close()