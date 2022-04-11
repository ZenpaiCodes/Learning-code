# COMPRENHENSIONS
# list, set, dictionary

my_list = []

for letter in 'wassap':
    my_list.append(letter)
print(my_list)

# list comprehension
my_list_comp = [letter for letter in 'wassap']
print(my_list_comp)

# my_list = [expresion, loop, if condition]
my_list_comp_num = [num for num in range(0, 101)]
print(my_list_comp_num)

my_list_comp_num_2 = [num * 2 for num in range(0, 101)]
print(my_list_comp_num_2)

my_list_comp_num_3 = [num ** 2 for num in range(0, 101) if num % 2 == 0]
print(my_list_comp_num_3)


# comprenhensive dictionary
simple_dict = {
    'k1': 100,
    'k2': 200,
    'k3': 301
}

my_dict = {key: value ** 2 for key, value in simple_dict.items() if value %
           2 == 0}
print(my_dict)


# EXERCISE
the_list = [ 'a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'i', 'j', 'a', 'd', 'e', 'f']

# append only unique values
duplicates = [letter for letter in set(the_list) if the_list.count(letter) > 1]
print(duplicates)

