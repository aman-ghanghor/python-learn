#  ============== Exception ==============
#
#  An exception is a runtime error which can be handled by the programmer.
#  All exception are represented as classes in Python.
#
#  Types of Exception:-
#  
#      * Built-in Exception - Exceptions which are already available in Python Language.
#                             The base class for All built-in exceptions is BaseException class.
#
#      * User Defined Exception - A programmer can create his own exceptions, called user-defined
#                                 exceptions.
#



#  ============== Need of Exception Handling =============
#
#     * When an exception occurs, the program terminates suddenly.
#
#     * Suddenly termination of program may corrupt the program.
#
#     * Exception may cause data loss from the database or a file.
#



#  ============== Exception Handling =============
#
#    Try - The try block contains code which may cause exceptions.
#
#    Except - The except block is used to catch an exception that is raised in the try block.
#             There can be multiple except block for try block.
#
#             Syntax:-       
#                     except ExceptionName:
#
#    Else - This block will get executed when no exception is raised. Else block is executed
#           after try block.
#
#           Syntax:- 
#                   else: 
#                        statements
#
#    Finally - This block will get executed irrespective of whether there is an exception or not.
#      
#              Syntax:-
#                      finally:
#                              statements
#



# NOTE -
#        * We can write several except blocks for a single try block.
#
#        * We can write multiple except blocks to handle multiple exceptions.
# 
#        * We can write try block without any except blocks.
#
#        * We can not write except block without a try block.
#
#        * Finally block is always executed irrespective of whether there is an exception or not.
#
#        * Else block is optional
#


#
#    try:
#        Statement
#    except ExceptionClassName:
#        Statement
#    else:
#        Statement
#    finally:
#        statement
#
#


#
#    try:
#        Statement
#    except ExceptionClassName1:
#        Statement
#    except ExceptionClassName2:
#        Statement
#    finally:
#        statement
#
#


#
#   try:
#      Statement
#



# ================ Except ================
#
#    * With the Exception Class Name
#
#          except ExceptionClassName:
#              Statement
#   
#
#    * Exception as an object 
#
#          except ExceptionClassName as obj:
#              Statement
#
#
#    * Multiple Exception within tuple
#             
#          except (ExceptionClassName1, ExceptionClassName2, ExceptionClassName3, ...):
#              Statement
#
#
#    * Catch any Type of Exception
#       
#          except: 
#              Statement
#




a = 10
b = 0
c = 5

try:
    d = a/b
    print(d)
    print('Inside try block')
except ZeroDivisionError as obj:
    # print("Division by zero is not allowed!")
    print(obj)
except NameError as obj:
    print(obj)
else:
    print("Inside else block")
finally:
    print("Inside finally block")

print("Rest of Error")











