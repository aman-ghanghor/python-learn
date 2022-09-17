# ========== Text Mode and Binary Mode ===========
#
# Text Mode = A file opened in text mode, treats it contents as if it contains text strings
#             of the str type
#             When you get data from a text mode file, Python first decodes the raw bytes 
#             using either a plateform-dependent encoding or, specified one.
#
#
# Binary Mode = A file opened in Binary Mode, Python uses the data in the file without
#               any decoding, binary mode file reflects the raw data in the file.


f = open('student.txt', mode='w')
f.write('Hello\n')
f.write('GeekyShows\n')
f.write('How are you')
f.close()
print('Writing Success')

f = open('student.txt', mode='r')
data = f.read()
print(data)
f.close()

f = open('student.txt', mode='rb')
data = f.read()
print(data)
f.close()






















