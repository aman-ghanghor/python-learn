#   map() Function = This function executes a specified function on each element
#                    of the iterable (sequence) and perhaps changes the elements.
#  
#   Syntax -
#           map(function_name, iterable)
#


myList = [10, 20, 30, 40]
print(myList, id(myList))

def func(item):
    return (item+5)

result = map(func, myList)        # map object
print(list(result))











