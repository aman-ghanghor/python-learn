# This function returns a table of current global variables in the form of dictionary

a = 50

def show():
    a = 10
    print("Local Variable A:", a)
    print(globals()['a'] + a)

show()
print("Global Variable A:", a)







