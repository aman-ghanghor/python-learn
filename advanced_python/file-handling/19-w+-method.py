# writing and then reading It will overwrite existing data

f = open('student.txt', mode='w+')

f.write("Youtube")  # file pointer goes to end of file

print(f.tell())   # file pointer after write

f.seek(0)   # send file pointer to the beginning of file

data = f.read()

print(data)













