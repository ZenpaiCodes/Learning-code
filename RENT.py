import calendar
import datetime

# timedelta is the difference between two dates
# *******CHANGE DATE HERE********
weeks = []
start_date = datetime.date(2022, 10, 26)


while len(weeks) < 15:
    weeks.append(start_date)
    end_date = start_date + datetime.timedelta(6)
    weeks.append(end_date)
    start_date = end_date + datetime.timedelta(1)


print(
    f'''
HAMPTON BAYS
{weeks[0]} to {weeks[15]}
AMERICAN LEGION 
55 Ponquogue Ave,
Hampton Bays NY 11946

DESCRIPTION
Payment of rent, the payment is for 8 weeks. The period starts on {weeks[0]} and ends on {weeks[15]}. Eight weeks in total, with a payment of $500.00 per week; the total amount paid is $4000.00 dollars.

FORMATTED DATE = YEAR - MONTH - DAY
•	Week 1: {weeks[0]} to {weeks[1]}
•	Week 2: {weeks[2]} to {weeks[3]}
•	Week 3: {weeks[4]} to {weeks[5]}
•	Week 4: {weeks[6]} to {weeks[7]}
•	Week 5: {weeks[8]} to {weeks[9]}
•	Week 6: {weeks[10]} to {weeks[11]}
•	Week 7: {weeks[12]} to {weeks[13]}
•	Week 8: {weeks[14]} to {weeks[15]}
                     $500 X 8 = $4000.00

With my name and signature, I, the landlord state that I have received the amount of money shown above.

NAME: ______________________________________

SIGNATURE: __________________________________

    '''
)