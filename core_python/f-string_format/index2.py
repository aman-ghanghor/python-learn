# ------------------------- Integer ---------------------------

#            :[fill][align][sign][#][0][width][,][.precision]type

num = 12
num1 = 1234567890

print( f"{num:8d}" )              # 5 = width

print( f"{num:08d}" )             # with padding

print( f"{num:+8d}" )             # sign

print( f"{num:+08d}" )            # sign, padding

print( f"{num:<8d}" )             # left align

print( f"{num:<08d}" )            # left align, padding

print( f"{num:>08d}" )            # right align, padding

print( f"{num:*<8d}" )            # left align, fill

print( f"{num:*>8d}" )            # right align, fill

print( f"{num:*^8d}" )            # right align, fill

print( f"{num:*^+8d}" )           # center align, fill, sign

print( f"{num1:,d}" )             # thousands separator






















