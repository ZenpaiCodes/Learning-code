# Error handling

try:
    age = int(input("How old are you? "))
    print(age)
except:
    # prevents the program from crashing.
    print("Please enter a number.")
else:
    print("Thank you.")
finally: #  Try/Except/finall is a way to handle errors.
    print('final step.')


# sum example

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:  # if any error occurs, this will run. err = error.
        print(f'\n\n{err}')


print(sum('1', 1))
