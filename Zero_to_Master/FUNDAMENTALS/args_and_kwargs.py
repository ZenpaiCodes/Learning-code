# *args **kwargs - arguments and keyword arguments
 
def my_func(*args): # args would take only one argument. Adding *args to the function would take multiple arguments.
    print(args) # args is a tuple.
    return sum(args) # sum of all arguments - sum is a function already defined in python
print(my_func(1,2,3,4,5)) # 1+2+3+4+5 = 15
