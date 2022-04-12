# Generator
def generator_func(num):  # Generator function.
    for x in range(num):  # Loop through the range of numbers.
        yield x*6  # yield will stop the function and return the value.


g = generator_func(2)  # Create a generator object.
# contrary to a list, a generatoe will keep only the last item in memory.
print(next(g))  # Get the next value.
print(next(g))  # Get the next value.
    # next() will return StopIteration if there is no next value.
# print(next(g))

 