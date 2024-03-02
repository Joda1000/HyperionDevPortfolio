"""
This program outputs one of two financial calculations,
based on user's selection and inputs.
"""

import math

WELCOME_MESSAGE = '''\nWelcome to the financial calculator. Please see the\
 calculations menu below:
    investment  - to calculate the amount of interest you'll earn on your\
 investment
    bond        - to calculate the amount you'll have to pay on a home loan\
\n'''

print(WELCOME_MESSAGE)

calculation = (input("Enter either 'investment' or 'bond' from the menu above\
 to proceed: "))
calculation = calculation.lower()


if calculation == "investment":
    deposit = float(input("\nPlease enter the amount you are depositing: "))
    interest_rate = float(input("Please enter the interest rate: "))
    interest_rate = interest_rate / 100
    years = float(input("Please enter the amount of years you plan on \
investing: "))
    interest = (input("Please specify if you want simple or compound \
interest: "))
    interest = interest.lower()

    if interest == "simple":
        total_amount = deposit * (1 + interest_rate * years)
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + interest_rate), years)
    else:
        print("Error: incorrect interest type provided.")
    

    print(f"\nYou will earn {total_amount:.2f} on your investment.")


elif calculation == "bond":
    house_value = float(input("\nPlease enter the value of your house: "))
    interest_rate = float(input("Please enter the interest rate: "))
    months = float(input("Please enter how many months you plan to take to \
repay the bond: "))
    monthly_interest = interest_rate / 100 / 12
    repayment = ((monthly_interest * house_value)/
                 (1 - (1 + monthly_interest)**(-months)))

    print(f"\nYou will need to repay {repayment:.2f} each month on your home \
loan.")

else:
    print("Error: invalid entry.")


    



