# *args **kwargs - arguments and keyword arguments
 
def my_func(*args, **kwargs): # args would take only one argument. Adding *args to the function would take multiple arguments.
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total # sum of all arguments - sum is a function already defined in python
print(my_func(1,2,3,4,5, num_1 = 5, num_2 = 10)) # 1+2+3+4+5 = 15

# Rule: params, *args, default parameters, **kwargs
