
person = {'name': 'Rahul', 'age': 22, 'city': 'Delhi'}
print(person, id(person))

man = person.copy() 
print(man, id(man))

man['name'] = "Sina"
print()

print(person, id(person))        # person dict is unchanged 
print(man, id(man))              # modified


