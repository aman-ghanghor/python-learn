#  In C, Java and some other languages we pass value to a function either by value or by reference widely
#  known as "Pass by Value" and "Pass by Reference".

#  In Python, neither of these two concepts is applicable rather the values are sent to functions by means 
#  of "object reference" (pass by object reference). we can also call it [pass by Assignment]

#  When we pass value like number, strings, tuples, or lists to function, the references of these objects 
#  are passed to function.

from traceback import print_tb


def val(x):
    print(x, id(x))      # x is 10, passed as object
    x = 15               # new object created as value of x changed, as Integer is immutable
    print(x, id(x))

x = 10
val(x)
print(x, id(x))
print()



def show(lst):
    print(lst, id(lst))
    lst[1] = 5                 # list objects are mutable, so lst will be modified
    print(lst, id(lst))

myList = [1, 2, 3, 4]
show(myList)
print(myList, id(myList))
print()



#  NOTE
#  In Python, values are passed to functions by object references.
#  If object is immutable (not modifiable) then the modified value
#  is not available outside the function

# Immutable (not modifiable) Objects - Integer, Float, String and Tuple
# Mutable Objects - List, Dictionary


def showMe(l):
    print(l, id(l))
    l = [10, 20, 30]        # l object changed after assignment 
    print(l, id(l))

newList = ['a', 'b', 'c']
print(newList, id(newList))
showMe(newList)
print(newList, id(newList))       # not modified outside function


# NOTE -
#  When we create a new object inside function then it will not be available outside function



