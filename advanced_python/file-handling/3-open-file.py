# ============= Opening a File ==============
#
#  If we want to use a file or its data, first we have to open it.
#
#  open() = Open() function is used to open a file. It returns a pointer to the beginning of the file.
#           This is called file handler or file object.
#
#  Syntax:-  open('filename', mode='r', buffering, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#
#    * filename = It represents a name of a file.
#
#    * mode = It represents the purpose of opening the file. It defaults to 'r' which means open
#             for reading in text mode.
#
#    * buffering = It is an integer value used to set the size of the buffer for the file. In the 
#                  binary mode we can pass 0 as buffering integer to inform not to use any buffering.
#                  In text mode we can pass 1 for buffering to retrieve data from the file one line at 
#                  a time. We can pass any positive integer. Default is 4096 or 8192 bytes.
#
#    * encoding = name of the encoding used to decode or encode the file. It should be used only in 
#                 text mode.
#                 Ex:- utf-8
#
#    * errors = an optional string that specifies how encoding and decoding errors are to be handled, 
#               this cannot be used in binary mode. Some of the standard values are strict, ignore,
#               replace etc.
#
#    * newline = this parameter controls how universal newlines mode works (it only applies to text mode).
#                It can be None, '', '\n', '\r', '\r\n'.
#
#    * closefd = If closefd is False and a file descriptor rather than a filename was given, the underlying
#                file descriptor will be kept open when the file is closed. If a filename is given closefd 
#                must be True (default) otherwise an error will be raised.
#
#    * opener = A custom opener can be used by passing a callable as opener.

#   f = open('student.txt', 'w')

#   f = open('D:\\myfolder\\student.txt', 'w')


f = open('student.txt', 'r') 
print(f)
