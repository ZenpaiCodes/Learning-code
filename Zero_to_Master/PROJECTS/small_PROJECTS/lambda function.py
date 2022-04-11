# lambda function
    # will not be stored in memory. They are anonymous functions.
    # they are used to create small functions that can be passed around.

my_list = [1, 2, 3, 4, 5]

print(list(map(lambda num: num ** 2, my_list)))

# list sorting based on second element in tuple
tuple_list = [(0,2), (4,3), (9,9), (10,-1)]
print(sorted(tuple_list, key=lambda second_num: second_num[1]))

