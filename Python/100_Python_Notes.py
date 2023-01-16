# Day 1
from asyncore import loop
from sre_constants import RANGE


len() # This would print how many characters are in the string
---------------------------------------------------
PRIORITY ORDER
#  PEMDAS
#  Parentheses - ()
#  Exponents - **
#  Multiplication - *
#  Division - /
#  Addition - +
#  Substraction - -
---------------------------------------------------
BAND NAME GENERATOR
#  print("Welcome to the band name generator")
#  City_name = input("What is the name of the city you grew up in? ")
#  Pet_Name = input("What is your pets name? ")
#  print(f"Your bands name could be: {City_name} {Pet_Name}")
---------------------------------------------------
Type conversion
#  First_Digit = int(two_digit_number[0])
#  Second_Digit = int(two_digit_number[1])
#  print( First_Digit + Second_Digit)
---------------------------------------------------
BMI Calculator
# height = input("What...")
# weight = input("What...")
# height_float = float(height)
# weight_float = float(weight)
# BMI = (weight_float / (height_float ** 2))
# print(int(BMI))
---------------------------------------------------
Your lifespan in days, weeks and months
# age = input("What is your current age? ")
# numeric_age = int(age)
# days_year = 365 * (90 - numeric_age)
# weeks_year = 52 * (90 - numeric_age)
# months_year = 12 * (90 - numeric_age)

# print(f"You have {days_year} days, {weeks_year} weeks, and {months_year} months left.")
---------------------------------------------------
Even or odd using % (moduler) if a number is devided by 2 with no remeinder is an even number.
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print ("This is an even number.")
# else:
#     print ("This is an odd number.")
---------------------------------------------------
Multiple conditionals
# A and B
# C or D 
# not E 
---------------------------------------------------
Random module
# import random	 

# heads_tales = random.randint(0, 1)
# if heads_tales == 1:
#     print("Heads")
# else:
#     print("Tails")
---------------------------------------------------
DATA STRUCTURE
# List
# variable = [item_1, item_2, item_3]
    # List order, positive numbers left to right, negative numbers right to left. [1] = item_1 vs [-1] = item_3
# variable.append(item_4) --> this will add oe item at the end of the list
# variable.extend([item_5, item_6, item_7]) --> this will add multiple items into the designated list
---------------------------------------------------
LOOPS
# fruits = ["apple", "pear", "pinapple"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
---------------------------------------------------
MAX and MIN function
# max()  --> will find HIGHEST number in a list
# min()  --> will find the LOWEST number in a list
---------------------------------------------------
RANGE
# for number in range(a, b):
#     print(number)
# for number in range(1, 10, 2): # first 2 numbers are the range, the third one is how big the step should be
#     print(number)

total = 0
for numbers in range(0, 101, 2): # Adding only even numbers
    total += numbers
print(total)
---------------------------------------------------
DEFINING THE FUNCTION
def my_function():
    # Do this
    # Then do this
    # Finally do this

CALLING THE FUNCTION
my_finction()

---------------------------------------------------
while loop
# while something_is_true:
    
# number_of_jumps = 6
# while number_of_jumps > 0:
#     jump()
#     number_of_jumps -= 1
---------------------------------------------------
FUNCTIONS
def my_function():
    # wherever the function does, no metter how long or short.
    # ................
    # ....................
---------------------------------------------------