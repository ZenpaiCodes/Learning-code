# dictionary
    # it's an unorder key value pick. vs list have an ordered position.
        # dictionaries can hold lists within it. Lists can hold doctionaries.
            # dictionary key most be inmutable. Example: srting, integer, boolean. ex NOT: list
dictionary = {
    'a' : 1,
    'c' : [1,2,3,4,5],
    'd' : 'hi',
    'e' : False,
    123 : [1, 2, 3],
    True : 'value'
}

# Game example dictionary use
user_diego = {
    'weapons' : None,
    'class' : ['warrior', 'mage', 'assasin'],
    'skills' : ['whirlwind', 'death strike', 'leap jump'],
}
print(user_diego['weapons'])

# DICTIONARY METHODS
# .get()
user = {
    'name' : 'Diego',
    'last_name' : 'Camacho',
    'age' : 18
}
print(user.get('age', 55)) # prints 18. Since age is assigned it prints its value.
                # if age not assign then assigns 55.

# .keys() checks if item is a key.
# .values() checks if item its a value.
# .items() grabs both keys and values.

# .popItem() removes last item inserted into the dictionary.

# .update() updates the dictionary
user.update({'age':64}) # use {} - If key and value not found in dict, it will add them.

