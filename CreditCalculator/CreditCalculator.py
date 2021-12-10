import math
import argparse

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
interest = args.interest * 0.01 / 12
payment = args.payment


def d():
    month = 0
    result = 0
    for m in range(1, periods + 1):
        month += 1
        diff_p = math.ceil(float(principal / periods) + interest * (principal - (principal * (m - 1)) / periods))
        print(f'Month {m}: payment is {math.ceil(diff_p)}')
        result += diff_p
    print(f"Overpayment {math.ceil(result - principal)}")


def n():
    monthly_payment_number = math.ceil(math.log(payment / (payment - interest * principal), interest + 1))
    years = monthly_payment_number / 12
    month = (years - math.floor(years)) * 12
    if math.floor(month) == 0:
        print(f"It will take {math.ceil(years)} years to repay this loan!")
    elif math.floor(month) != 0:
        print(f"It will take {math.floor(years)} years and {math.ceil(month)} months to repay this loan!>")
    else:
        print(f'It will take {math.ceil(month)} months to repay this loan!')
    overpayment = payment * monthly_payment_number - principal
    print(f'Overpayment = {overpayment}')
    # ceil - округляет в большую сторону, floor в меньшую


def a():
    period = pow(1 + interest, periods)
    monthly_payment = principal * ((interest * period) / (period - 1))
    print(f"Your monthly payment = {math.ceil(monthly_payment)}!")
    print(f"Overpayment {math.ceil(monthly_payment) * periods - principal}")


def p():
    period = pow(1 + interest, periods)
    loan_p = math.floor(payment / (interest * period / (period - 1)))
    print(f"Your loan principal = {math.floor(loan_p)}!")
    overpayment = payment * periods - loan_p
    print(f'Overpayment = {overpayment}')


try:
    if typee == "annuity":
        if payment is not None and principal is not None:
            if principal > 0 and payment > 0 and interest > 0:
                n()
            else:
                print("Incorrect parameters")
        elif principal is not None and periods is not None:
            if principal > 0 and periods > 0 and interest > 0:
                a()
            else:
                print("Incorrect parameters")
        elif payment is not None:
            if payment > 0 and periods > 0 and interest > 0:
                p()
            else:
                print("Incorrect parameters")
    elif typee == "diff":
        if principal > 0 and periods > 0 and interest > 0:
            d()
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
except TypeError:
    print("Incorrect parameters")


# print('''
# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# ''')
# choice = input()
