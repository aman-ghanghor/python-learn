# ========== Writes Data to the file  ==========
# 
#  write() = This method is used to store/write character or string into the file 
#            represented by the file object. It returns the number of character written
#            Syntax:-  file_object.write(string)


f = open('student.txt', mode='w')

n = f.write("Hello world\n")
f.write("How are are you\n")
f.write("Hope you are good?")
print(n)

f.close()



