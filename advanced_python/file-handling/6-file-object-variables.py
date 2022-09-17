# ==========  File object Variables  ============
#   
#   name = This shows the name of specified file.
#          syntax:-  file_object.name
#
#   mode = This shows mode (purpose) of the file.
#          syntax:-  file_object.mode
#
#   closed = This used to check whether file has closed or not.
#            It shows True if file is closed else shows False.
#            syntax:-  file_object.closed
#   



# ==========  File object Variables  ============
#   
#   readable() =  This method is used to check whether file is readable or not.
#                 It returns True if file is readable else returns False.
#                 Syntax:-  file_object.readable()
#
#   writable() =  This method is used to check whether file is writable or not, 
#                 It returns True if file is writable else returns False.
#                 Syntax:-  file_object.writable()

f = open('student.txt', mode='r', encoding='utf-8')

print("name:", f.name)
print("mode:", f.mode)
print("closed:", f.closed)
print("encoding:", f.encoding)

print()

print("readable =", f.readable())
print("writable =", f.writable())

f.close()

print()
print("closed:", f.closed)














