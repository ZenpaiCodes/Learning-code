import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
random_position = random.randint(0, num_items - 1)

random_name = names[random_position]

print(f"{random_name} is going to buy the meanl today!")



# USING .choice example 
# print("Draw One fully awaken UR guaranteed!")
# February_draws = ['Goku', 'Naruto', 'Vegeta', 'Broly', 'Netzuko', 'Freezer', 'Sasuke']

# import random

# UR_random = random.choice(February_draws)
# print(UR_random)