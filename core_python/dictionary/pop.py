# ----------- pop() method ------------
#
#  This method is used to remove the item with specified key.
#  It returns the removed item's value.
#  If key is not found then the a default value is returned.
#  If key is not found and default value is not given then show KeyError.
#
#  Syntaxt:-   dict_name.pop(key, defaultValue)


stu = {101: 'Rahul', 102: 'Sonam', 103: 'Meera'}
print(stu)

result = stu.pop(103, "student")
print(result)
print(stu)

















