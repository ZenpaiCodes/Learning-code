# Pizza Size
S_pizza = 15
M_pizza = 20
L_pizza = 25
# Add ons
S_pepperoni = 2
M_L_pepperoni = 3
extra_cheese = 1

bill = 0

print("Welcome to Python Pizza Deliveries!")

answer_size = input("What size pizza do you want? S, M, or L ")
pepperoni_add = input("Do you want pepperoni? Y or N ")
cheese_add = input("Do you want extra cheese? Y or N ")

if answer_size == "S":
    bill = S_pizza
    if pepperoni_add == "Y":
        bill += S_pepperoni
    if cheese_add == "Y":
        bill += extra_cheese
    print(f"Your final bill is: ${bill}.")

if answer_size == "M":
    bill = M_pizza
    if pepperoni_add == "Y":
        bill += M_L_pepperoni
    if cheese_add == "Y":
        bill += extra_cheese
    print(f"Your final bill is: ${bill}.")

if answer_size == "L":
    bill = L_pizza
    if pepperoni_add == "Y":
        bill += M_L_pepperoni
    if cheese_add == "Y":
        bill += extra_cheese
    print(f"Your final bill is: ${bill}.")