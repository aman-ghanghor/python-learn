# ------------------  Files  -------------------
#
#  File is the collection of data that is available to a program. We can retrieve and use 
#  data stored in a file whenever we required.

# ------------- Advantages :-
# 
#   1. Stored Data is permanent unless someone remove it.
#   2. Stored data can be shared.
#   3. It is possible to update or remove the data.


# ------------- Types of Files ----------------
#
# - There are two type of files:-
#
#   1. Text File = It stores data in the form of characters. It is used to store characters and strings.
#   
#   2. Binary File = It stores data in the form of bytes, a group of 8 bit each. It is used to store 
#                    text, images, pdf, csv, video and audio.


f = open('student.txt', mode='w')
f.write('Hello How are you?')

f.close()