# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
rows = [            # when iterating over multiple lists, use plural variable.
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '*'
empty = ' '

for row in rows:  # singular variable for the plural.
    for pixel in row:
        if pixel == 0:
            print(empty, end='')
        else:
            print(fill, end='')
    print('')
