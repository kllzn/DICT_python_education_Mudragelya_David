import math

print("Enter the loan principal:")
principal = int(input())
print('What do you want to calculate?'
      'type "m" – for number of monthly payments,'
      'type "p" – for the monthly payment:')
choice = input()
if choice == "m":
    print('Enter your monthly payment:')
    user_payment = int(input())
    duration = principal//user_payment
    print(f'It will take {duration} months to repay the loan')
elif choice == "p":
    print('Enter the number of months:')
    months = float(input())
    mpayment = math.ceil(principal/months)
    last_payment = math.ceil(principal - (months - 1) * mpayment)
    print(f'Your monthly payment = {mpayment} and the last payment = {last_payment}')