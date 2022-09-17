# ------------- Accessing Argument Items ------------------

value = (10, 20, 30)
person = {'name': 'Rahul', 'age': 19, 'money': 4090.23}

print( "{0[0]} kg Matar, {0[1]} kg Mango".format(value) )

print( "{0[1]} kg Mater, {0[0]} kg Mango".format(value) )

print( "His name is {0[name]}. He is {0[age]} year old. his bank balance is {0[money]:.2f}".format(person) )

print( "His name is {p[name]}. He is {p[age]} year old. his bank balance is {p[money]:.2f}".format(p=person) )

print( "His name is {name}. He is {age} year old. his bank balance is {money:.2f}".format(**person) )














