# We can delete an item of dictionary or entire dictionary using del statement.

person = {'name': "Rahul", 'age': 21, 'city': 'Delhi'}

print(person, id(person))

del person['city']                # delete item

print(person, id(person))

# del person                      # delete dictionary

