# ------------------------ Integer ------------------------

#        :[fill][align][sign][#][0][width][,][.precision]type    


print( "{num:5d}".format(num=12) ) 

print( "{num:05d}".format(num=12) )

print( "{num:+05d}".format(num=12) )

print( "{num:+5d}".format(num=12) )

print( "{num:<05d}".format(num=12) )

print( "{num:>05d}".format(num=12) )

print( "{num:<5d}".format(num=12) )

print( "{num:>5d}".format(num=12) )

print( "{num:*<5d}".format(num=12) )

print( "{num:@>5d}".format(num=12) )

print( "{num:^5d}".format(num=12) )

print( "{num:^6d}".format(num=12) )

print( "{num:^05d}".format(num=12) )

print( "{num:^06d}".format(num=12) )

print( len("{num:5d}".format(num=12)) ) 


#   5 = width
#   d = type
#   0 = padding
#   + = sign
#   <, > = align ( < = left align, > = right align )
#   *(any character) = fill (NOTE- align should be used to use fill)
#   ^ = center



























