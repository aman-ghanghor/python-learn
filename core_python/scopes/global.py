# When a variable is declared above a function, it becomes global variable.
# Thse variables are available to all the function which are written after it.
# The scope of global variable is the entire program body written below it.

a = 50   # Global variable

def show():
    x = 10
    print(a)
    print(x)

show()