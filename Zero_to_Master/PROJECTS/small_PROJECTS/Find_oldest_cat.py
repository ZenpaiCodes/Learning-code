# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_1 = Cat('Garfield', 6)
cat_2 = Cat('Tom', 20)
cat_3 = Cat('Yoruichi', 1000)

# 2 Create a function that finds the oldest cat


def find_oldest_cat(*args): # *args is a tuple. It can take multiple arguments. 
    return max(args) # max is a function already defined in python.


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f"The oldest cat is {find_oldest_cat(cat_1.age, cat_2.age, cat_3.age)} years old.")


# EX: another possible solution
# def oldest_cat():
#     oldest = cat_1.age
#     if cat_2.age > oldest:
#         oldest = cat_2.age
#     if cat_3.age > cat_2.age:
#         oldest = cat_3.age
#     return oldest
