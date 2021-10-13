from collections import Counter

amounts = Counter({'water_amount': 400, 'milk_amount': 540, 'beans_amount': 120, 'money_amount': 550, 'cups_amount': 9})


def remaining():
    print('The coffee machine has:\n'
          ' {} of water\n'.format(amounts.get('water_amount')),
          '{} of milk\n'.format(amounts.get('milk_amount')),
          '{} of coffee beans\n'.format(amounts.get('beans_amount')),
          '{} of disposable cups\n'.format(amounts.get('cups_amount')),
          '{} of money'.format(amounts.get('money_amount')))
    __action__()


def take():
    print('I gave you {}'.format(amounts.get('money_amount')))
    amounts['money_amount'] = 0
    print('')
    __action__()


def fill():
    your_fill = {'water_amount': 0, 'milk_amount': 0, 'beans_amount': 0, 'cups_amount': 0}

    water_amount = int(input('Write how many ml of water you want to add:'))
    your_fill.update({'water_amount': -water_amount})

    milk_amount = int(input('Write how many ml of milk you want to add:'))
    your_fill.update({'milk_amount': -milk_amount})

    beans_amount = int(input('Write how many grams of coffee beans you want to add:'))
    your_fill.update({'beans_amount': -beans_amount})

    cups_amount = int(input('Write how many disposable coffee cups you want to add:'))
    your_fill.update({'cups_amount': -cups_amount})

    amounts.subtract(your_fill)
    print('')
    __action__()


def buy():
    choose = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')

    if choose == '1':
        espresso = Counter({'water_amount': 250, 'beans_amount': 16, 'cups_amount': 1, 'money_amount': -4})
        if amounts['water_amount'] < espresso['water_amount']:
            print('Sorry, not enough water!')
        elif amounts['beans_amount'] < espresso['beans_amount']:
            print('Sorry, not enough beans!')
        elif amounts['cups_amount'] < espresso['cups_amount']:
            print('Sorry, not enough cups!')
        else:
            amounts.subtract(espresso)
            print('I have enough resources, making you a coffee!')
        print('')
        __action__()
    elif choose == '2':
        latte = Counter({'water_amount': 350, 'beans_amount': 20, 'cups_amount': 1, 'money_amount': -7, 'milk_amount': 75})
        if amounts['water_amount'] < latte['water_amount']:
            print('Sorry, not enough water!')
        elif amounts['beans_amount'] < latte['beans_amount']:
            print('Sorry, not enough beans!')
        elif amounts['cups_amount'] < latte['cups_amount']:
            print('Sorry, not enough cups!')
        elif amounts['milk_amount'] < latte['milk_amount']:
            print('Sorry, not enough milk!')
        else:
            amounts.subtract(latte)
            print('I have enough resources, making you a coffee!')
        print('')
        __action__()
    elif choose == '3':
        cap = Counter({'water_amount': 200, 'beans_amount': 12, 'cups_amount': 1, 'money_amount': -6, 'milk_amount': 100})
        if amounts['water_amount'] < cap['water_amount']:
            print('Sorry, not enough water!')
        elif amounts['beans_amount'] < cap['beans_amount']:
            print('Sorry, not enough beans!')
        elif amounts['cups_amount'] < cap['cups_amount']:
            print('Sorry, not enough cups!')
        elif amounts['milk_amount'] < cap['milk_amount']:
            print('Sorry, not enough milk!')
        else:
            amounts.subtract(cap)
            print('I have enough resources, making you a coffee!')
        print('')
        __action__()


def __action__():
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        buy()
    elif action == 'take':
        take()
    elif action == 'fill':
        fill()
    elif action == 'exit':
        game_exit()
    elif action == 'remaining':
        remaining()
    else:
        __action__()


def game_exit():
    pass


__action__()


# print('Starting to make a coffee\n'
#       'Grinding coffee beans\n'
#       'Boiling water\n'
#       'Mixing boiled water with crushed coffee beans\n'
#       'Pouring coffee into the cup\n'
#       'Pouring some milk into the cup\n'
#       'Coffee is ready!')
