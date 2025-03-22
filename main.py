###
# This code simulates a mock a budget. I find it interesting because I am moving and my expenses will
# be changing I am wieghing how to make budget changes to adjust.
###

print()
import random

def get_input():
    monthly_income = float(input("What is your monthly income? $"))
    rent = float(input("How much is your rent? $"))
    food = float(input("What do you spend on average for food? $"))
    transportation = float(input ("How much do you spend on transportation? $"))
    entertainment = float(input("How much do you spend on leasurly activities? $"))

    expenses = rent + food + transportation + entertainment

    return monthly_income, expenses



def interest_calc():
    investment_return = 0
    investments = float(input("\nHow much would you like to invest this month? $"))
    if investments > 0:
        interest_rate = random.randint(-9,9)
        investment_return += investments * (1 + (interest_rate/100))
    elif investments == 0:
        print("You chose not to invest this month.")
    
    return investment_return
    



def main():
    monthly_income, expenses = get_input()
    total = 0
    proceed = True
    while proceed:

        investment_return = interest_calc()

        net_worth = monthly_income - expenses + investment_return

        total += net_worth
        print("Your return from your investment:",investment_return)
        print (f"\nYour current balance is: ${total:.2f}")

        proceed_response = input("\nWould you like to continue? (yes or no)")

        if proceed_response != 'yes':
            proceed = False
            print("\nHave a good day and make wise choices.")

main()
