# with variables

a = "Rahul"
b = 18

print("My name is {0:s}. I am {1:d} year old".format(a, b))

print("My name is {name:s}. I am {age:d} year old".format(name=a, age=b))

print("My name is {name:s}. I am {age:d} year old".format(age=b, name=a))