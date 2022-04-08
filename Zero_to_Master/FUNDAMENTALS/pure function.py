# pure function
# will always retun the same result for the same input
# no side effects
from functools import reduce


def multiple_by_two(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiple_by_two([1, 2, 3]))

# map()
# map() is a function that takes a function and a list as input and returns a list with the function applied to each item in the list.
my_list = [1, 2, 3]


def multiple_by_three(item):
    return item * 3


print(list(map(multiple_by_three, [1, 2, 3])))  # map() returns a map object.

# filter()


def check_if_odd(num):
    return num % 2 != 0


# filter() returns a filter object.
print(list(filter(check_if_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# zip()
his_list = ['a', 'b', 'c']
her_list = ['d', 'e', 'f']

# zip() returns a zip object. Acts very much like a zipper.
print(list(zip(his_list, her_list)))

# reduce()
a_list = [1, 2, 3, 4, 5]


# acc is the accumulator, item is the item in the list. acc defult value is 0.
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, a_list, 0))
# 10 is the initial value of the accumulator.
print(reduce(accumulator, a_list, 10))
