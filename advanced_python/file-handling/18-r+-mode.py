# Read then Write
f = open('student.txt', mode='r+')

print(f.tell())
data = f.read()
print(f.tell())

f.write('Youtube')
print(f.tell())

print(data)


