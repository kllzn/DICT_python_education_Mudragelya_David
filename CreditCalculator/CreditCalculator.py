import math
import argparse

# забыл схранить 3 этап, поэтому вот промежуточный между 3 и 4

parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--annuity", type=float)
parser.add_argument("--type", type=str)
args = parser.parse_args()
typee = args.type
principal = args.principal
periods = args.periods
interest = args.interest / 1200
payment = args.payment


def d():
    month = 0
    result = 0
    for m in (1, periods + 1):
        month += 1
        diff_p = math.ceil(float(principal / periods) + interest * (principal - (principal * (m - 1)) / periods))
        print(f'Month {str(m)}: payment is {math.ceil(diff_p)}')
        result += diff_p
        print(f"Overpayment {math.ceil(result - principal)}")

def start():
    choose = input(f"""What do you want to calculate?
        type "n" for number of monthly payments,
        type "a" for annuity monthly payment amount,
        type "p" for loan principal:\n >""")
    if choose == "n":
        n()
    if choose == "a":
        a()
    if choose == "p":
        p()


def n():
    loan_p = int(input("Enter the loan principal:"))
    monthly_payment = int(input("Enter the monthly payment"))
    loan_i = float(input("Enter the loan interest:"))
    i = loan_i * 0.01 / 12
    monthly_payment_number = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_p), i + 1))
    years = monthly_payment_number / 12
    month = (years - math.floor(years)) * 12
    if math.floor(years) == 0:
        print(f"It will take {math.ceil(years)} years to repay this loan!")
    else:
        print(f"It will take {math.floor(years)} years and {math.ceil(month)} months to repay this loan!>")
        # ceil - округляет в большую сторону, floor в меньшую


def a():
    loan_p = int(input("Enter the loan principal:"))
    number_periods = int(input("Enter the number of periods:"))
    loan_i = float(input("Enter the loan interest:"))
    i = loan_i * 0.01 / 12
    monthly_payment = loan_p * ((i * (pow(1 + i, number_periods))) / (pow(1 + i, number_periods) - 1))
    print(f"Your monthly payment = {math.ceil(monthly_payment)}!")


def p():
    annuity_p = float(input("Enter the annuity payment:"))
    number_periods = int(input("Enter the number of periods:"))
    loan_i = float(input("Enter the loan interest:"))
    i = loan_i * 0.01 / 12
    loan_p = annuity_p / ((i * (pow(1 + i, number_periods))) / (pow(1 + i, number_periods) - 1))
    print(f"Your loan principal = {math.floor(loan_p)}!")


# print('''
# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# ''')
# choice = input()

start()
