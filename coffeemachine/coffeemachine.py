class CoffeeMachine:

    def __init__(self):
        # amounts = Counter(
        #     {'water_amount': 400, 'milk_amount': 540, 'beans_amount': 120, 'money_amount': 550, 'cups_amount': 9})
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.money = 550
        self.cups = 9

    def take(self):
        if self.money == 0:
            print('There is no money')
        else:
            print(f'I gave you {self.money}')
            self.money = 0

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add:'))
        self.milk += int(input('Write how many ml of milk you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans you want to add:'))
        self.cups += int(input('Write how many disposable coffee cups you want to add:'))

    def make_espresso(self):
        # espresso = Counter({'water_amount': 250, 'beans_amount': 16, 'cups_amount': 1, 'money_amount': -4})
        if self.water < 250:
            print('Sorry, not enough water!')
        elif self.beans < 16:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        else:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            print('I have enough resources, making you a coffee!')
        print('')

    def make_latte(self):
        # latte = Counter(
        #     {'water_amount': 350, 'beans_amount': 20, 'cups_amount': 1, 'money_amount': -7, 'milk_amount': 75})
        if self.water < 350:
            print('Sorry, not enough water!')
        elif self.beans < 20:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        elif self.milk < 75:
            print('Sorry not enough milk!')
        else:
            self.water -= 350
            self.beans -= 20
            self.cups -= 1
            self.milk -= 75
            self.money += 7
            print('I have enough resources, making you a coffee!')
        print('')

    def make_cappuccino(self):
        # cap = Counter(
        #     {'water_amount': 200, 'beans_amount': 12, 'cups_amount': 1, 'money_amount': -6, 'milk_amount': 100})
        if self.water < 200:
            print('Sorry, not enough water!')
        elif self.beans < 12:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        elif self.milk < 100:
            print('Sorry not enough milk!')
        else:
            self.water -= 200
            self.beans -= 12
            self.cups -= 1
            self.milk -= 100
            self.money += 6
            print('I have enough resources, making you a coffee!')
        print('')

    def remaining(self):
        print(f'The coffee machine has:\n'
              f'{self.water} of water\n',
              f'{self.milk} of milk\n',
              f'{self.beans} of coffee beans\n',
              f'{self.cups} of disposable cups\n',
              f'{self.money} of money')


functions = CoffeeMachine()


def buy():
    choose = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    if choose == '1':
        functions.make_espresso()
    elif choose == '2':
        functions.make_latte()
    elif choose == '3':
        functions.make_cappuccino()
    elif choose == 'back':
        actions()


def actions():
    while True:
        action = input('Write action (buy, fill, take, remaining, exit):')
        if action == 'buy':
            buy()
        elif action == 'fill':
            functions.fill()
        elif action == 'take':
            functions.take()
        elif action == 'remaining':
            functions.remaining()
        elif action == 'exit':
            break


actions()
