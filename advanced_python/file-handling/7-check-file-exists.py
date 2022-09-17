# ============= Check File Exists or not ==============
#
#  isfile() = This method is used to check whether specified file is existing or not.
#             This method belongs to path module which is sub module of os module.
#             Ex :-
#                   import os
#                   os.path.isfile(filename)

import os

if(os.path.isfile('student.txt')):
    f = open('student.txt', mode='r', encoding='utf-8')
    print(f.read())
    f.close()
else:
    print("File not exists!!!")