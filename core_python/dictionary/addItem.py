# -------------- Inserting / Adding new item ---------------
#
#   We can add an item to dictionary just by mentioning a new key-value pair into an existing dictionary.
#
#   If we mention a key which is already exists in the dictionary then the value gets updated/modified
#   rather then adding a new item.
#
#   The new item may be added at any place in the dictionary as dictionary is an unordered collection.


person = {'name': 'Rahul', 'age': 21, 'city': 'Delhi'}

print(person, id(person))

person['city'] = "Mumbai"       # modified

print(person, id(person))

person['PIN'] = 123456          # new item added

print(person, id(person))








