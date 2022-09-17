# Note: If the item to remove does not exist, discard() will NOT raise an error.

myset = {'apple', 'banana', 'mango'}

print(myset, id(myset))

myset.discard('orange')    # will not raise error, even 'orange' not exist in set

print(myset, id(myset))

myset.discard('banana')

print(myset, id(myset))