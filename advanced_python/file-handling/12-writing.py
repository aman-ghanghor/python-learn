f = open('student.txt', mode='a')

lst = ['Tom\n', 'Jerry\n']
f.writelines(lst)

f.close()