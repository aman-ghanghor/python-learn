# ------------------------ Float ------------------------

#        :[fill][align][sign][#][0][width][,][.precision]type    

print( "{}".format(15.65) )

print( "{:f}".format(15.65) )

print( "{0:f}".format(15.65) )

print( "{num:f}".format(num=15.65) )

print( "{num:8.3f}".format(num=15.65) )        # .3 is precision

print( "{num:+8.2f}".format(num=15.65) )        # .2 is precision

print( "{num:<8.2f}".format(num=15.65) )       # left align

print( "{num:*<8.2f}".format(num=15.65) )      # left align with fill

print( "{num:*>8.2f}".format(num=15.65) )      # right align with fill













# NOTE-1 = float takes 6 digit after decimal
# NOTE-2 = decimal point (dot .) also takes one digit space

#   8 = width
#   d = type
#   0 = padding
#   + = sign
#   <, > = align ( < = left align, > = right align )
#   *(any character) = fill (NOTE- align should be used to use fill)
#   ^ = center








