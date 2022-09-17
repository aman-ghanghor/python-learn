# ============  with Statement  ============
#
#  The with statement can be used while opening a file.
#  When we open a file using with statement there is no need to close the file
#  explicitly
#
#  Syntax:-   
#          with open('filename', mode='r') as file object:
#                 statements
#


with open('student.txt', mode='r') as f:
    data = f.read()
    print(data)
    print(f.closed)
    
print(f.closed)