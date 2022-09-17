# ------------------------ String ------------------------

#        :[fill][align][sign][#][0][width][,][.precision]type   


print( "{:.3}".format("GeekyShows") )         # first three character (precision)

print( "{:8.3}".format("GeekyShows") )         # 8 box precision to 3

print( "{:>8.3}".format("GeekyShows") )        # 8 box, precision 3, right align

print( "{:<8.3}".format("GeekyShows") )        # 8 box, precision 3, left align

print( "{:>08.3}".format("GeekyShows") )        # 8 box, precision 3, right align, padding

print( "{:*<8.3}".format("GeekyShows") )        # 8 box, precision 3, left align, fill 

print( "{:*^8.3}".format("GeekyShows") )        # 8 box, precision 3, fill, center





