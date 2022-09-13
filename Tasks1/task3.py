"""
Loan payment calculator
"""

# Get the details of the loan from the user: How much money do you owe, in dollars?​
money_owed = input('How much money do you owe, in dollars? ')

# Convert input to float​
money_owed = float(money_owed)

# Get the annual percentage rate: what us the annual percentage rate?​
apr = float(input('What is the annual percentage rate? '))

# Get the monthly payment: what will your monthly payment be, in dollars?​
payment = float(input('What will your monthly payment be, in dollars? '))

# Get  months to calculate results: how many months do you want to see the results for?​
months = int(input('How many months do you want to see the results for? '))

# Repeat the calculation for all the months the user  wants to see results for​
for i in range(months):
    # Divide annual percentage rate by 100 to make it a percent, then divide by 12 to get the monthly insterest rate
    #   monthly_rate = apr/100/12
    monthly_rate = apr/100/12

    # add in  interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    # Make payment
    money_owed = money_owed - payment
    # Print the results 
    print("\nPaid", payment, "of which", interest_paid, "was interest")
    print("Now, I owe", money_owed)



# add control to check if money_owed - payment < 0 then print messages and break repetition
if money_owed - payment < 0:
    print("the last payment is", money_owed)
    print("You pay off the loan in", months, "months")
else:
    # round the dollar amount to two decimals   
    money_owed = round(money_owed, 2)

    print("The final amount you owe is", money_owed)

