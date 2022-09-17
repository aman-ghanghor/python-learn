# ------------ If the item to remove does not exist, remove() will raise an error -----------

myset = {'apple', 'banana', 'orange'}

print(myset, id(myset))

# myset.remove('mango')              # raise error, it mango is not there in set

myset.remove('banana')

print(myset, id(myset))