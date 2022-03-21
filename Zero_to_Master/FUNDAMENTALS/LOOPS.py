# LOOPS
    # for
from turtle import bye


inventory = ['food', 'medicine', 'weapon']

# for variable in iterable
    # iterable is an object over which we can perform iterations over and over.
for items in inventory: # the iterable can be a string, dictionary, list, variable, set, tuple,
    print(items) 

for items_2 in (1,2,3,4,5):
    for i in ['a','b','c']:
        print(items_2, i)
print(items_2)
print(i)


# Lopping over DICTIONARY
box = {
    'fruits': ['apple', 'pear'],
    'scraps': 'paper',
    'pen': 'blue'
}

for item in box: # only prints keys.
 # for item in box.keys()
    print(item) 

for item in box.items(): # prints keys values.
    print(item)

for item in box.values(): # prints values.
    print(item)

for key, value in box.items(): # commun practice when trying to print keys and values.
    print(key, value)


# EXCERCISE
    # loop over each value in list and add them up.
numbers = [1,2,3,4,5,6,7,8,9,10] 
sum = 0 # this variable must be outside of the loop. Because if it was inside, everytime the loop starts it would be reset vack into its original value.

for item in numbers:
    sum += item
print(sum)
# EXCERCISE FINISHED

# range() 
print(range(0, 100))

for i in range(10 + 1):
    print(i) # prints 0,1,2...10

for _ in range(0, 11, 2): # prints from 0 to 11 in intervals of 2.
    print(_)

for n in range(0, 10, -1): # won't print anything as it will try to go backwards from 0 to 9.
    print(n)
for x in range(10, 0, -1): # print from 10 to 1
    print(x)

# enumerate()
for char in enumerate('Hello World!'): 
    print(char) # index and its position.

# EXCERCISE
    # find index of number 50 in a numeric list.
position = enumerate(list(range(40, 100)))
    # SOLUTION 1
for x in position:
    if 50 in x:
        a, b = x
        if b == 50:
            print(f'index of number 50 in this list is: {a}')
    # SOLUTION 2
position = enumerate(list(range(40, 100)))
for x, num in position:
    print(x, num)
    if num == 50:
            print(f'index number of 50 in this list is: {x}')
# EXCERCISE COMPLETED

# while Loop
i = 0 
while i < 50: # while is a loop with a condition.
    i += 1
    print(i)
else:
    print('Done with all the work.') 
    
    # Break
while True:
    response = input('say something: ')
    if response == 'bye':
        break

    # continue for loops and while loops
for_list = [1,2,3]
i = 0

for i in for_list:
    i += 1
    print(i)
    print('here')
    continue # continue will return code to the first line of the loop
    print('done')

    # pass is a place holder.
for _ in for_list:
    # Not sure yet.
    pass # pass is preventing the code from breaking