# walrus operator
# https://docs.python.org/3/library/operator.html#operator.walrus

a = 'whasaaaaaaaaaaaaap'

if (length := len(a)) > 12:
    print(f"this string has {length} characters. It\'s way to long!")

while (length := len(a)) > 5:
    print(length)
    print(a)
    a = a[:-1]
print(a)