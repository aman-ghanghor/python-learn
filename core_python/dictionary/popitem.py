# ---------- popitem() ------------
#
#  This method is used to remove the item which was last inserted into the dictionary
#
#  It returns the removed item in the form of tuple, Pairs are returned in LIFO order.
#
#  Syntax:-  dict_name.popitem()


stu = {101: 'Rahul', 102: 'Raj', 103: 'Meera'}
print(stu)

item = stu.popitem()
print(stu)
print(item)
print(type(item))










