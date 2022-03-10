#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to the tip calculator")

bill = input("What was the total bill? ")
num_bill = float(bill)

falt_tip = input("How much tip would you like to give: 10%, 12%, 15% or 18%? ")
num_tip = (float(falt_tip) / 100)
total_tip = (num_bill * num_tip)

party_size = input("How many people to split the bill? ")
num_party_size = float(party_size)

# Bill + tip 
total_price = float(num_bill + total_tip)

# Each one pays the following
each_pay = round(total_price / num_party_size, 2)
two_digit_each_pay = format(each_pay, ".2f")

print(f"Each person would pay: ${format(two_digit_each_pay)}")


# print("Welcome to the tip calculator!!!\nPlease tell us")

# bill = input("How much is the bill? ")
# num_bill = float(bill)

# tip = input("What percentage tip would you like to give: 10%, 12%, 15%, 18% ? ")
# decision_tip = float(tip)
# total_tip = num_bill * (decision_tip / 100)

# bill_plus_tip = num_bill + total_tip

# party_size = input("Among how many people should we split it? ")
# num_party_size = int(party_size)

# final_contribution = round(bill_plus_tip / num_party_size, 2)
# two_digit_contribution = format(final_contribution, ".2f")

# print(f"Each person should pay: ${two_digit_contribution}")