# Module 4 Lab
# Riceli Foster
# 02/25/24
# This program calculates a company's bonus as well as the individual bonuses.

monthlySales = 0 #monthly sales amount
storeAmount = 0 #store bonus amount
empAmount = 0 #employee bonus amount
salesIncrease = 0 #percent of sales increase
prompt = str("Enter monthly sales.\n")

monthlySales = float(input(prompt))

if monthlySales > 110000:
    storeAmount = 6000
elif monthlySales >= 100000 and monthlySales < 110000:
    storeAmount = 5000
elif monthlySales >= 90000 and monthlySales < 100000:
    storeAmount = 4000
elif monthlySales >= 80000 and monthlySales < 90000:
    storeAmount = 3000
else:
    storeAmount = 0

#Converts user's input to a percentage. 
salesIncrease = float(input("Enter sales increase.\n"))
salesIncrease = salesIncrease / 100

#Determines if sales increase is going to receive a bonus for each individual employee.
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#Display results.
print("The store bonus amount is $",storeAmount)
print("The employee bonus amount is $",empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have  reached the higest bonus amounts possible!')
