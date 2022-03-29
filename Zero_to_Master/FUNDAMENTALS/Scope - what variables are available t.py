# Scope - what variables are available to the function

# 4th is sum a python built in function? = YES
a = 20
# 3rd is sum in global? = NO
def parent(): # 2nd is sum in parent()? = NO
    def example():
        return sum # 1st is sum in function? = NO
    return example()

print(parent())
print(a)

# This is the order in which the variables are defined:
# 1- Start with local
# 2- Parent local?
# 3- Global
# 4- Built-in python functions.

# To use a global variable in a function, you must use the global keyword before the variable name.
total = 0

def counter():
    global total
    total += 1
counter()
counter()
print(total)

# Global - variables defined outside of the function
# Global variables can be accessed by all functions in the program
# Local - variables defined inside of the function
# Local variables can only be accessed by the function they are defined in
# Nonlocal variables can be accessed by any function in the program
# Nonlocal variables can only be accessed by the function they are defined in
# Nonlocal - variables defined in a parent function

# remove white space from a string.
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_ref_string.asp
x = "   Hello World   "
print(x.strip()) # will remove white space from the string.
# return a string in upper case letters
# methos to replace parts of a string
# https://www.w3schools.com/python/ref_string_replace.asp
y = x.replace(" ", "")
