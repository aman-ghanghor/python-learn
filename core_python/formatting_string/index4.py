# ------------------------ String ------------------------

#        :[fill][align][sign][#][0][width][,][.precision]type    

print( "{:8s}".format("Geek") )

print( "{0:8s}".format("Geek") )

print( "{str:8s}".format(str="Geek") )

print( "{str:<8s}".format(str="Geek") )         # Left align

print( "{str:>8s}".format(str="Geek") )         # Right align

print( "{str:>08s}".format(str="Geek") )        # padding

print( "{str:*>8s}".format(str="Geek") )        # Right align with fill

print( "{str:*^8s}".format(str="Geek") )         # center align with fill







#   8 = width
#   d = type
#   0 = padding
#   + = sign
#   <, > = align ( < = left align, > = right align )
#   *(any character) = fill (NOTE- align should be used to use fill)
#   ^ = center



