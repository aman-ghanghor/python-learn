# ---------------- Generator function -----------------
#
#   Generators are functions that return a sequence of values. We use yield statement to return 
#   the value from function.


# ---------------- Yield Statement ------------------
#
#   Yield statement returns the elements from a generator function into a
#   generator object.
#
#   Ex:-  yield a

# ----------------- next() function ------------------
#
#   This function is used to retrieve element by element from a generator object.
# 
#   Syntaxt:-   next(gen_obj)


def disp(a, b):
    while a<=b:
        yield a
        a += 1

result = disp(1, 5)           # return generator object
print(result, id(result))

# myList = list(result)          # convert generator object into list object
# print(myList, id(myList))


# Accessing generator item using next() function

print(next(result))
print(next(result))
print()

for i in result:
    print(i)
