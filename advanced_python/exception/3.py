a = 10
b = 0
c = 5


try:
    d = a/b
    print(d)
    print('Inside try block')
except ZeroDivisionError:
    print("Infinity")



print("Rest of Error")