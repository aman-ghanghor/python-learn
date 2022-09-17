# Appending and then reading It won't overwrite existing data

f = open('student.txt', mode='a+')

print(f.tell())

f.write("Amritsar")

print(f.tell())          # file pointer goes to end of file after appending.

f.seek(0)

print(f.tell())

data = f.read()

print(data)







