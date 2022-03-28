# Scope - what variables are available to the function

a = 20

def parent():
    def example():
        return sum
    return example()

print(parent())
print(a)


# This is the order in which the variables are defined:
# 1- Start with local
# 2- Parent local?
# 3- Global
# 4- Built-in python functions.


# Global - variables defined outside of the function
# Global variables can be accessed by all functions in the program
# Local - variables defined inside of the function
# Local variables can only be accessed by the function they are defined in
# Nonlocal variables can be accessed by any function in the program
# Nonlocal variables can only be accessed by the function they are defined in
# Nonlocal - variables defined in a parent function

