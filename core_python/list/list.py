# Lists are - 

# 1. ordered
# 2. changeable
# 3. allow duplicate values
# 4. list items are indexed


myList = ["banana", "orange", "grapes", "banana", "banana"]

# Allow Duplicates
# print(myList)


# List Length
# print(len(myList))


# List Items - Data Types
# myList1 = [1, 2, 3]
# myList2 = ["banana", "orange", "apple"]
# myList3 = [True, False, False]
# myList4 = [1, 2, "banana", True]


# type() = lists are defined as objects with the data type 'list'
# print(type(myList))


# list() constructor = It is also possible to use the list() constructor when creating a new list.
# myList = list(("apple", "banana", "orange"))
# print(myList)


# ----------------------- Access Items -------------------------
# myList = ['apple', 'banana', 'cherry', 'mango']
# print(myList[2])
# print(myList[-1])           # Starts from end (-1 = last item)
# print(myList[1:3])
# print(myList[:3])
# print(myList[1:])



#---------------------- Change Item Value -----------------------
# myList = ['apple', 'banana', 'cherry', 'mango']
# myList[1] = "orange"
# print(myList)

# --------------- Change a Range of Item Values -------------
# myList = ['apple', 'banana', 'cherry', 'mango']
# myList[1:3] = ["papaya", "guava"]
# print(myList)

# ---------- Insert more items than you replace -----------
# myList = ['apple', 'banana', 'cherry', 'mango']
# myList[1:3] = ['A', 'B', 'C'] 
# print(myList)

# ---------- Insert less items than you replace -----------
# myList = ['apple', 'banana', 'cherry', 'mango']
# myList[1:3] = ['A'] 
# print(myList)



# ----------- Inserts new item at specified index ------------
# myList = ['apple', 'banana', 'cherry']
# myList.insert(2, 'watermelon')
# print(myList)


# ----------- Append Items ------------
# myList = ['apple', 'banana', 'cherry']
# myList.append('A')
# print(myList)


# --------- To append elements from another list to the current list ---------
# myFruits = ['apple', 'banana', 'cherry']
# myVegs = ['Aalu', 'Gobhi', 'Matar'] 
# myFruits.extend(myVegs)
# print(myFruits)


# ------- Add Any Iterable -------
# thisList = ['apple', 'banana', 'cherry']
# thisTuple = ['Matar', 'Gobhi']
# thisList.extend(thisTuple)
# print(thisList)




# ========== Remove List Items ============

# -------- Remove Specified Item --------
# thisList = ['apple', 'cherry', 'banana']
# thisList.remove('banana')
# print(thisList)

# -------- Remove Specified Index --------
# thisList = ['apple', 'cherry', 'banana']
# thisList.pop(1)
# print(thisList)

# -------- Remove Last Item --------
# thisList = ['apple', 'cherry', 'banana']
# removedItem = thisList.pop()
# print(thisList)

# -------- del keyword also remove the specified index -------
# myFruits = ['apple', 'cherry', 'banana']
# del myFruits[1]
# print(myFruits)

# ------- The del keyword can also delete the list completely -------
# myFruits = ['apple', 'cherry', 'banana']
# del myFruits

# ------- Clear the List -------
# myFruits = ['apple', 'cherry', 'banana']
# myFruits.clear()
# print(myFruits)





# ------- Loop List -------
# myFruits = ['apple', 'cherry', 'banana', 'orange']
# for x in myFruits:
#     print(x)

# ------ Loop through Index Number ------
# myFruits = ['apple', 'cherry', 'banana', 'orange']
# for x in range(len(myFruits)):
#     print(myFruits[x])

# ------ Using while loop ------
# myFruits = ['apple', 'cherry', 'banana', 'orange']
# x = 0
# while(x < len(myFruits)):
#     print(myFruits[x])
#     x += 1

# A short hand for loop that will print all items in a list
# myFruits = ['apple', 'cherry', 'banana']
# [print(x) for x in myFruits]






# 









# Note - There are four collections data types in Python
# 1. List 
# 2. Tuple
# 3. Set
# 4. Dict






















