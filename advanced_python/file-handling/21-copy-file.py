
f1 = open('student.txt', mode='r')
f2 = open('student1.txt', mode='w')

data = f1.read()

f2.write(data)

f1.close()
f2.close()