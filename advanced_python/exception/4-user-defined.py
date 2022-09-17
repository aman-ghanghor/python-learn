#  ============= User Defined Exception =============
#
#  A programmer can create his own exceptions, called user-defined exceptions or custom Exception.
#
#    * Creating Exception Class using Exception Class as a Base Class
#
#    * Raising Exception
#
#    * Handling Exception



# ============ Creating Exception ============
#
#  class MyException(Exception):
#      pass
#
#
#  class MyException(Exception):
#      def __init__(self, arg):
#         self.msg = arg 
#
#
#




# =========== Raising Exception ==============
#
#  raise statement is used to raise the user defined exception
#
#  Syntax:-
#        raise MyException('Message')
#



# =========== Handling Exception ==============
#
#  try:
#      statement
#  
#  except MyException as mye:
#      statement
#
#


class BalanceException(Exception):
    pass


def checkbalance():
    money = 10000
    withdraw = 9000
    try:
        balance = money - withdraw
        if(balance <= 2000):
            raise BalanceException("Insufficient Balance")
        print(balance)
    except BalanceException as be:
        print(be)



checkbalance()