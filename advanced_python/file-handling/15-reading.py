f = open('student.txt', mode='r')

data = f.readlines()

print(data)
print()

for i in data:
    print(i, end='')

f.close()