# ------------------ String ------------------

#           :[fill][align][sign][#][0][width][,][.precision]type


name = "Geek"

print(f"{name:8s}")                # default left align

print(f"{name:>8s}")               # right align

print(f"{name:<8s}")               # left align

print(f"{name:0>8s}")              # right align, padding

print(f"{name:0<8s}")              # left align, padding

print(f"{name:*>8s}")              # right align, fill with *

print(f"{name:*<8s}")              # left align, fill with *

print(f"{name:*^8s}")              # center align, fill with *

print()

str1 = "GeekyShows"

print( f"{str1:.4s}" )

print( f"{str1:$<8.4s}" )          # truncate, left align, fill with $

print( f"{str1:$>8.4s}" )          # truncate, right align, fill with $

print( f"{str1:$^8.4s}" )          # truncate, center align, fill with $




