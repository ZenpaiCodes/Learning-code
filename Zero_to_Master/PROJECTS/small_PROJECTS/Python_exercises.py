# EXERCISE 1:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
num_list = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        num_list.append(num)


print(num_list, end=',')

# EXERCISE 2:
# Write a program which can compute the factorial of a given numbers.
