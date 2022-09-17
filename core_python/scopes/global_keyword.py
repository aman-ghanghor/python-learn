# If local variable and global variable has same name then the function by
# default refers to the local variable and ignores the global variable.

# It means global variable is not accessible inside the function but possible to
# access outside of function

# In this situation, If we need to access global variable inside the function we
# can access it using global keyword followed by variable name.

name = "Rahul"
a = 10

def show():
    global a 
    a = a + 1
    print("A =", a)       

show()


