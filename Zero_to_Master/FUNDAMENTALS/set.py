# SET 
    # A set holds only unique items. Value will not be repited.
my_set = {1,2,3,4,5,5,5,6,7,8,8}
# print(my_set) # Will print {1,2,3,4,5,6,7,8} no duplicates.

# LIST into SET 
my_list = {1,2,3,4,5,5}
new_set = set(my_list)
# print(new_set) # Will print {1,2,3,4,5}

# list methods
set_1 = {1,2,3,4,5,5}
set_2 = {1,2,3,'word','string',5}
set_3 = {1,5,'no','yes'}
set_4 = {4,5,6,7,8,9,10,11,12,13}
set_5 = {6,7,8}
    
    # difference 
print(set_1.difference(set_2)) # will print the difference between both list (checks for int not string), DOES NOT REMOVES, just TELLS.
    
    # discard
print(set_2.discard('word')) # will remove given value from set.
print(set_2)
    
    # .difference_update()
print(set_3.difference_update(set_2)) # compares set_3 to set_2. removes from (set_2) similar items. REMOVES
print(set_3)

    # .intersection() -- &
print(set_1.intersection(set_4)) # will print items where set intersects.
        # print(set_1 & set_4) # == example above

    # .isdisjoit()
print(set_1.isdisjoint(set_4)) # prints False if the have something in commun. prints True if they dont have nothing in commun.

    # union() == |
print(set_2.union(set_3)) # units sets.
        # print(set_2 | set_3) # == example above

    # issubset()
print(set_5.issubset(set_4)) # are all the elements of set_5 found in set_4? True or False. (True)

    # issuperset() 
print(set_5.issuperset(set_4)) # does set_5 holds all the items in set_4 and more? True or False. (False)
