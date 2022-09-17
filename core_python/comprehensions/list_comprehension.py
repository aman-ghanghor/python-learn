# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# newlist = [expression for item in iterable if condition == True]


lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

new_lst1 = [ (x+1)*2 for x in lst1 ]

new_lst2 = [ (x+1)*2 for x in range(20) ]

new_lst3 = [ (x*2) for x in range(20) if x%2==0 ]

print(new_lst1)
print(new_lst2)
print(new_lst3)







