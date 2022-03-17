# TUPLE
    # They are like list but cannot be modifed. They are inmutable.
my_tuple = (1,2,3,3,3,3,4,5)
# my_tuple[2] = 'change' --> ERROR tuple does not support change.

# .count() 
print(my_tuple.count(3)) # prints 4, number of times value repeats.

# .index()
print(my_tuple.index(2)) # prints position in tuple.

# len()
print(len(my_tuple)) # prints lenght of tuple.
