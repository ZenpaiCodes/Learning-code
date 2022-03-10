year = int(input("Which year do you want to check? "))

if year % 400 == 0:
    print("Leap year.")
elif year % 4 == 0 and year % 100 == 0:
    print("Not leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not leap year.")




# year = int(input("Which year do you want to check? "))

# a = year % 4
# b = year % 100
# c = year % 400

# # Nesting

# if b and c == 0:
#     print("Leap year.")
# elif a and b == 0:
#     print("Not leap year.")
# elif a == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")
