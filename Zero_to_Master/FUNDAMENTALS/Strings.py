num = "12345678" # string values cannot be reasign.Ex: num[3] = 9 WOULD CREATE AN ERROR
    #  01234567

# STRING slicing
print(num[0:6:2]) # num[start:stop:stepover] - Default values = [0:last item:step over]
                                             # To reverse items use -  Ex: [0::-1] -> Wpuld print items from last to the first one.


len(num) # FUNCTION
print(len(num))

    # STRING METHODS
sentence = "thIs iS a senTENce"
print(sentence.upper()) # all letters get upper case
print(sentence.capitalize()) # first letter gets capitalized the rest is lower cased
print(sentence.lower()) # everything gets lower cased