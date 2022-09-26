# Exercise function:

# print highest even number from a list
def highest_number(list_of_numbers):
    highest = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            if number > highest:
                highest = number
    return highest
print(highest_number([20,1,2,3,4,5,6,7,8,9,10]))

# print highest odd number from a list
def highest_odd(list_numbers):
    highest = 0
    for number in list_numbers:
        if number % 2 != 0:
            if highest < number:
                highest = number
    return highest

print(highest_odd([3,4,5,6,7,8,11,121,1,4,5,0]))

