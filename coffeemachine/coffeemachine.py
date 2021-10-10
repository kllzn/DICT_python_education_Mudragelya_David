
def variables():
    water_amount = 400
    milk_amount = 540
    beans_amount = 120
    money_amount = 550
    cups_amount = 9
    return water_amount, milk_amount, beans_amount, money_amount, cups_amount


def amount():
    water_amount, milk_amount, beans_amount, money_amount, cups_amount = variables()
    print('The coffee machine has:\n'
          f'{water_amount} of water\n'
          f'{milk_amount} of milk\n'
          f'{beans_amount} of coffee beans\n'
          f'{cups_amount} of disposable cups\n'
          f'{money_amount} of money')


amount()


def take():
    water_amount, milk_amount, beans_amount, money_amount, cups_amount = variables()
    print(f'I gave you {money_amount}')
    money_amount = 0
    print('')
    print('The coffee machine has:\n'
          f'{water_amount} of water\n'
          f'{milk_amount} of milk\n'
          f'{beans_amount} of coffee beans\n'
          f'{cups_amount} of disposable cups\n'
          f'{money_amount} of money')


def fill():
    water_amount, milk_amount, beans_amount, money_amount, cups_amount = variables()
    water_amount = water_amount + int(input('Write how many ml of water you want to add:'))
    milk_amount = milk_amount + int(input('Write how many ml of milk you want to add:'))
    beans_amount = beans_amount + int(input('Write how many grams of coffee beans you want to add:'))
    cups_amount = cups_amount + int(input('Write how many disposable coffee cups you want to add:'))
    print('The coffee machine has:\n'
          f'{water_amount} of water\n'
          f'{milk_amount} of milk\n'
          f'{beans_amount} of coffee beans\n'
          f'{cups_amount} of disposable cups\n'
          f'{money_amount} of money')


def buy():
    water_amount, milk_amount, beans_amount, money_amount, cups_amount = variables()
    choose = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    if choose == '1':
        water_amount -= 250
        beans_amount -= 16
        money_amount += 4
        cups_amount -= 1
        print('The coffee machine has:\n'
              f'{water_amount} of water\n'
              f'{milk_amount} of milk\n'
              f'{beans_amount} of coffee beans\n'
              f'{cups_amount} of disposable cups\n'
              f'{money_amount} of money')
    elif choose == '2':
        water_amount -= 350
        milk_amount -= 75
        beans_amount -= 20
        money_amount += 7
        cups_amount -= 1
        print('The coffee machine has:\n'
              f'{water_amount} of water\n'
              f'{milk_amount} of milk\n'
              f'{beans_amount} of coffee beans\n'
              f'{cups_amount} of disposable cups\n'
              f'{money_amount} of money')
    elif choose == '3':
        water_amount -= 200
        milk_amount -= 100
        beans_amount -= 12
        money_amount += 6
        cups_amount -= 1
        print('The coffee machine has:\n'
              f'{water_amount} of water\n'
              f'{milk_amount} of milk\n'
              f'{beans_amount} of coffee beans\n'
              f'{cups_amount} of disposable cups\n'
              f'{money_amount} of money')


def __action__():
    action = input('Write action (buy, fill, take):')
    if action == 'buy':
        buy()
    elif action == 'take':
        take()
    elif action == 'fill':
        fill()


__action__()


# print('Starting to make a coffee\n'
#       'Grinding coffee beans\n'
#       'Boiling water\n'
#       'Mixing boiled water with crushed coffee beans\n'
#       'Pouring coffee into the cup\n'
#       'Pouring some milk into the cup\n'
#       'Coffee is ready!')
