# Functions are subprograms which are used to compute a value or perform a task.

# TYPE OF FUNCTIONS :-

# 1. Built-in Function
# 2. User-defined Function




# def my_function():
#     print("Hello World")

# my_function()
# print()




# def sum(a, b):
#     result = a + b 
#     return result

# print(sum(2, 5))




# If you do not know how many arguments that will be passed into your function, add a * before 
# the parameter name in the function definition.
# def sum(*nums):
#     print(nums)
#     result = 0
#     for x in nums:
#         result += x
#     print(result)

# sum(1, 3, 5, 7)





# Keyword Argument
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# def func(child1, child2, child3):
#     print("child1 =", child1)
#     print("child2 =", child2)
#     print("child3 =", child3)

# func(child3="Rohit", child1="Meera", child2="Sonam")





# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# def func(**args):
#     print(args)
#     for x in args:
#         print(x)

# func(name="Rahul", age=23, city="Indore")





# Default Parameter Value
# def intro(name, age, country="India"):
#     print("name =", name)
#     print("age =", age)
#     print("country =", country)

# intro(name="Saroj", age=32)





# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# myLists = ['banana', 'cherry', 'papaya']
# def func(list):
#     print(list)
#     for x in list:
#         print(x)

# func(myLists)





# Pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
# def myFunction():
#     pass





# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# def func(k):
#     if(k==0):
#         print("Good Bye")
#     else:
#         print(k)
#         func(k-1)

# func(5)






# multiple returns
def getResult(a, b):
    add = a + b
    sub = b - a
    return add, sub

add, sub = getResult(5, 8)
print(add)
print(sub)





















