
# Sort List Alpha-numerically
# myFruits = ["orange", "banana", "apple", "mango", "guava"]
# myFruits.sort()
# print(myFruits)


# Sort List Numerically
# myList= [14, 7, 32, 12, 5, 3, 21]
# myList.sort()
# print(myList)


# Sort Descending - to sort descending use reserve keyword
# myList= [14, 7, 32, 12, 5, 3, 21]
# myList.sort(reverse=True)
# print(myList)




# Customise Sort Function 
# Sort the list based on how close the number is to 50:
# def myfunc(n):
#     return abs(n - 50)

# myList = [14, 7, 32, 12, 5, 3, 21]
# myList.sort(key=myfunc)
# print(myList)




# Case sensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)




# Luckily we can use built-in functions as key functions when sorting a list.
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)




# Reverse Order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)