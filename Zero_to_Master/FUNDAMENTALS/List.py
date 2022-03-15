list_1 = [
    1,
    2,
    3,
    4
    ] # can hold numbers

list_2 = [
    "string", 
    "house", 
    "car", 
    "sing", 
    "Eyyyy"
    ] # can hold strings

list_3 = [
    1,
    2,
    "string",
    True,
    False
    ] # elements of the list can be mixed upper

# LIST slicing
print(list_1[0:2]) # will print 1st and secn item
print(list_3[0::2]) # will pritn 1st and skip every other item

# To COPY a list
list_4 = list_3[:] # By having [:] we are copying the content of list_3 into list_4.
                # if not included. if we modify list_4 it would also modify list_3.

# MATRIX
list_5 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(list_5[0][2]) # prints 3

# ADDING
list_1.append(100) # adds 100 to the end of the list

# EXTEND
list_1.extend([101,102]) # extends the list with given values
print(list_1)

# INSERT
list_3.insert(4, 100) # list_3 now is [1,2,"string",True,100,False]
print(list_3)

# REMOVING 
list_1.pop() # .pop() removes the last item in the list
list_1.pop(0) # removes item in given position 
print(list_1) 

list_5.clear() # clear removes every item in the list 

# INDEX
list_3.index("string", 0, 4) # index finds the position in the list of the item.
                       # where the search starts and where it ends. DEFAULT is whole list.

# in
print("string" in list_3) # prints True, since item is in list. else: False

# count
print(list_3.count("string")) # prints 1. counts how many time that item occurs in the list.

# sorting
list_1.sort() # will sort items in list. CANNOT mix int and Strings
    # OR
# ----> THIS IS ALSO KNOWN AS LIST SLICING - [::]
print(sorted(list_1)) # Produces a new arrey, but the list itself IS NOT MODIFIED. (creates a new copy of the list) list_10 = list_1[:]
# same as print(list_1[::])
   
# reverse
list_3.reverse() # reverses items in list last one becomes first one and so on.

# RANGE 
print(list(range(1, 100))) # prints [1, 2, 3, 4, ... 99]

# JOIN 
joined_sentence = "!".join(["hi","my","name","is","Diego"]) # prints hi!my!name!is!Diego  - joins strings together with determined value.

# LIST UNPACKING 
a, b, c = [1, 2, 3] # a=1, b=2, c=3