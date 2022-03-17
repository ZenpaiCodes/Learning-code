# conditional statements

    # if statements
        # if will only run if -if- it's True
statement = True
statement_2 = False

if statement: # if statement = True then run this...
    print("statement is true")
elif statement_2:
    print("this statement is also true")
else: # if or elif statements are not true, then do this.
    print("else would be true")

    # and
if statement and statement_2:
    print("both conditions are true")
else:
    print("one or both conditions are false")

# Ternary operator
    # shorter version of the if statement
is_friend = False
can_message = "message is allowed" if is_friend else "CANOT MESSAGE. You can only message friend."
print(can_message)

# short circuting.
    # when using and / or python will check avoid unnecessary work ex:
if statement or statement_2:
    print("First statement is True, no need to check the second conditon!") # short circuting.
# another example. SHORT CIRCUTING.
print(1 < 2 < 3 > 4 < 5 < 6) # prints false and breaks reading at 3>4 since it's False there is no need to read the rest.

# EXCERCISE: ****************************
is_magician = False
is_expert = False

if is_magician and is_expert:
    print('you are a master magician.')
elif is_magician:
# elif is_magician and not is_expert:
    print('At least your getting there.')
elif is_expert:
    print('You need magic powers.')
else:
    print('This is the start of your journey')

# is
    # checks if item is in the same location in memory.
print(1 is 1) # prints True
print('4' is '4') # prints True
print([] is []) # prints False as a new list would be store in a new location.