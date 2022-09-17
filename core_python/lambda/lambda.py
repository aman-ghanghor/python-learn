# Lambda function is small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression



# Ex-1 (single arguments)
# x = lambda a : a + 10
# print(x(5))



# Ex-2 (multiple arguments)
# sum = lambda a, b : print(a + b)
# sum(5, 2)



# Ex-3 
def showName(num, n):
    result  = n(num, 3)
    print(result)

a = 5
showName(a, lambda x, times : x*times)

