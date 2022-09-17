# --------- setdefault() Method -----------
#
#  This method returns the value of the specified key.
#  If key is not found then it inserts key with the specified value.
#
#  Syntax:- dict_name.setdefault(key, value)


stu = {101: 'Rahul', 102: 'Sonam', 103: 'Meera'}

returned_value = stu.setdefault(102)
print(returned_value)
print(stu)
print()

returned_value1 = stu.setdefault(106, "Kalu")
print(returned_value1)
print(stu)