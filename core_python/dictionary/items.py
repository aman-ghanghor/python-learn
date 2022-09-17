# ------------ items() Method -------------
#
#   This method returns an object that contains key-value pairs of dictionary.
#   The pairs are stored as tuples in the object.
#
#   Syntaxt:-   dict_name.items()

person = {'name': 'Rahul', 'age':25, 'city': 'Delhi'}

result = person.items()   # return dict_items object

print(result)
print( type(result) )
print()

resultList = list(result)
print( resultList[0][1] )









