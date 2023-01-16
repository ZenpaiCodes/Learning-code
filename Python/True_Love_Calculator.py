print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Find out how many time TRUE can be found in both names 
lower_name1 = name1.lower()
lower_name2 = name2.lower()
names_true = lower_name1.count("t") + lower_name1.count("r") + lower_name1.count("u") + lower_name1.count("e") + lower_name2.count("t") + lower_name2.count("r") + lower_name2.count("u") + lower_name2.count("e")
#print(names_true)

#Find out how many time LOVE can be found in both names 
lower_name1 = name1.lower()
lower_name2 = name2.lower()
names_love = lower_name1.count("l") + lower_name1.count("o") + lower_name1.count("v") + lower_name1.count("e") + lower_name2.count("l") + lower_name2.count("o") + lower_name2.count("v") + lower_name2.count("e")
#print(names_love)

# TRUE LOVE count variable
true_love = int(str(names_true) + str(names_love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# #True Love name 1
# Lower_case_name1 = name1.lower()
# Lower_case_name1.count("t")
# Lower_case_name1.count("r")
# Lower_case_name1.count("u")
# Lower_case_name1.count("e")
# True_count_1 = Lower_case_name1.count("t") + Lower_case_name1.count("r") + Lower_case_name1.count("u") + Lower_case_name1.count("e")
# #print(f"True_count_1 = {True_count_1}")

# Lower_case_name1.count("l")
# Lower_case_name1.count("o")
# Lower_case_name1.count("v")
# Lower_case_name1.count("e")
# Love_count_1 = Lower_case_name1.count("l") + Lower_case_name1.count("o") + Lower_case_name1.count("v") + Lower_case_name1.count("e")
# #print(f"Love_count_1 = {Love_count_1}")

# #True Love name 2
# Lower_case_name2 = name2.lower()
# Lower_case_name2.count("t")
# Lower_case_name2.count("r")
# Lower_case_name2.count("u")
# Lower_case_name2.count("e")
# True_count_2 = Lower_case_name2.count("t") + Lower_case_name2.count("r") + Lower_case_name2.count("u") + Lower_case_name2.count("e")
# #print(f"True_count_2 = {True_count_2}")

# Lower_case_name2.count("l")
# Lower_case_name2.count("o")
# Lower_case_name2.count("v")
# Lower_case_name2.count("e")
# Love_count_2 = Lower_case_name2.count("l") + Lower_case_name2.count("o") + Lower_case_name2.count("v") + Lower_case_name2.count("e")
# #print(f"Love_count_2 = {Love_count_2}")

# # Results converted into Strings
# Love_score_1 = str(True_count_1 + True_count_2)
# Love_score_2 = str(Love_count_1 + Love_count_2)
# Love_score_total = Love_score_1 + Love_score_2
# # Result converted back into integer
# Love_score_total = int(Love_score_total)

# # Print results under conditionals
# if Love_score_total < 10 or Love_score_total > 90:
#     print(f"Your score is {Love_score_total}, you go together like coke and mentos.")
# elif Love_score_total >= 40 and Love_score_total <= 50:
#     print(f"Your score is {Love_score_total}, you are alright together.")
# else:
#     print(f"Your score is {Love_score_total}")

