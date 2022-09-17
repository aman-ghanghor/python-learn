# A Decorator function is a function that accepts a function as parameter and returns a function.

# A decorator takes the result of a function, modifies the result and return it.

# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

# We use @function_name to specify a decorator to be applied on another function




# def decor(fun):
#     def inner():
#         print("Before Enhancing Function")
#         fun()
#         print("After Enhancing Function")
#     return inner

# def num():
#     print("We will use this function")
#     print("and will enhance this in decorator")

# result_fun = decor(num)
# result_fun()
# print();





# ------------ Decorator function ------------------

# def decor(fun):
#     def inner():
#         print("Before Enhancing Function")
#         fun()
#         print("After Enhancing Function")
#     return inner

# @decor
# def num():
#     print("We will use this function")
#     print("and will enhance this in decorator")

# num()





# ---------------- example ---------------

def decor(fun):
    def inner():
        a = fun()
        add = a + 5
        return add 
    return inner
@decor
def num():
    return 10

print(num())
















