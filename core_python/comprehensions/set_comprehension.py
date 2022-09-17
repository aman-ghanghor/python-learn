import csv
# ------------- Set Comprehension ----------------
#
#   Set comprehension represents creation of new set from an iterable object that satisfy a given condition.
#
#   Syntax:-    {expression for item in iterable_object if_statement}

set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

new_set1 = {i*2 for i in set1}

new_set2 = {i*2 for i in set1 if i%2==0}

new_set3 = {i*2 for i in range(20) if i%2==0 if i%3==0}

print(new_set1)
print(new_set2)
print(new_set3)
