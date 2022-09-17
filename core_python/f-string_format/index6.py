# ------------- Expression --------------

from multiprocessing.sharedctypes import Value


print( f"8*3" )

print( f"{8*3}" )

print()





# ------------- Percentage --------------

a = 8
b = 3

print( f"{a/b:.2f}" )

print( f"{b/a:.2%}" )

print()





# -------------- Excessing Items --------------

value = (10, 20, 30)
person = {'name': 'Meera', 'age': 21}

print( f"{value[1]} {value[2]}" )

print( f"My girlfriend's name is {person['name']}. She is {person['age']} years old" )

print()




# -------------- use Function inside format string -----------------
name = "Rahul"

print(f"{name.upper()}")

print()



# ---------------- Using curly braces -----------------

print(f"{ {10} }")






