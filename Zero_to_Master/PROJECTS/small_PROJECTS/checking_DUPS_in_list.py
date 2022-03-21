# Check for duplicate in list.
# if duplicate found add unique to duplicates
list_with_dups = ['a', 'b', 'c', 'a', 'd', 'e', 'd', 'e']

duplicates = []

for letter in list_with_dups:
    if list_with_dups.count(letter) > 1:
        if letter not in duplicates:
            duplicates.append(letter)

print(duplicates)