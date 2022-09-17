#   reduce() Function = This function is used to reduce a sequence of elements to a single value by
#                       processing the elements according to a function supplied. It returns a single
#                       value.
#  
#   This function is a part of functools module so you have to import it 
#   before using.
#
#   Syntax:-
#           from functools import reduce
#           reduce(function_name, sequence)



from functools import reduce

myList = [1, 2, 3, 4, 5]

result = reduce(lambda m,n : m+n, myList)       # return single value

print(result)
print(type(result))













