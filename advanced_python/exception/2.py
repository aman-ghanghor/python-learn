
a = 10
b = 0
c = 5


try:
    d = a/b
    print(d)
    print('Inside try block')
except (ZeroDivisionError, NameError) as obj:
    print("Except handler")
    print(obj)



print("Rest of Error")
