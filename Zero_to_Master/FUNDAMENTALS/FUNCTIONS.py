def my_function():
    print(1 + 1)

# call the function
my_function()

    # parameters and arguments.
# PARAMETERS = variables been used inside the function -DEFINE THE FUNCTION-
def say_hello(name, emoji):
    print(f'helloooo! {name} {emoji}')

# positional ARGUMENTS = the actual value we provide to the function -CALL THE FUNCTION-
say_hello('Diego', '😜')

# KEYWORD arguments
say_hello(emoji = '😜', name = 'Diego') # BAD PRACTICE

# DEFAULT values
def player_1(name = 'Goku', skill = 'Spirit Bomb'):
    print(f'Your name is {name} and your ultimate skill is {skill}')

player_1() # if parameters are not defined, python will use defult
player_1('Freezer', 'Death ray')

# RETURN 
def sum(num1, num2):
    return num1 + num2 # without return value would be None when printed

total = sum(4, 9) # 13
print(sum(4, total)) # 4 + 13


# EXERCISE
        # age = input("What is your age?: ")

        # if int(age) < 18:
        # 	print("Sorry, you are too young to drive this car. Powering off")
        # elif int(age) > 18:
        # 	print("Powering On. Enjoy the ride!");
        # elif int(age) == 18:
        # 	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age = 0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(age = int(input("How old are you? ")))
# EXERCISE COMPLETED

# Docstrings
def test(a): # comment under is how we comment in a function so that teammates can find out what the function does faster.
    '''
    Info: this function test and prints param a
    '''
    print(a)

test('function_variable')
help(test) # Helps find out what a function does

# lambda functions
# lambda functions are functions that are defined without a name.
# lambda functions are used to create anonymous functions.
x = lambda a, b: a + b # x is a function that adds a and b.