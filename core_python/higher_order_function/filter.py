#   filter() Function = The filter function is used to filter out the elements of an iterable (sequence) 
#                      depending on a function that tests each element in the sequence to be true or not.
#                      It returns those elements of sequence, for which function is true. 

#  Syntax - 
#          filter(function_name, iterable)

#  Function_name = It's name of a function which tests each element in the sequence return True or False.
#                  If function is None, returns the elements that are true.
#
#  iterable = Iterable may be either a sequence, list, string, tuple, a container which supports iterable, or an iterator.


ageList = [12, 7, 38, 23, 65, 14, 15, 25]

def filterAge(age):
    if age>=18:
        return True
    else:
        return False

filteredObj = filter(filterAge, ageList)   # return filter object
print(filteredObj)
print(type(filteredObj))
print()


filteredList = list(filteredObj)           # convert into list object
print(filteredList)
print(type(filteredList))



# Using lambda function

# filteredObj = filter(lambda age: (age>=18), ageList )










































