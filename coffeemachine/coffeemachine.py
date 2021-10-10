import time

# cups = int(input('Write how many cups of coffee you will need:'))
# print('For {} cups of coffee you will need:\n'.format(cups),
#       '{} ml of water\n'.format(cups * 200),
#       '{} ml of milk\n'.format(cups * 50),
#       '{} g of coffee beans'.format((cups * 15)))
# time.sleep(1)

water_amount = int(input('Write how many ml of water the coffee machine has:'))
milk_amount = int(input('Write how many ml of milk the coffee machine has:'))
beans_amount = int(input('Write how many grams of coffee beans the coffee machine has:'))
cups = int(input('Write how many cups of coffee you will need:'))
can_make = [water_amount // 200, milk_amount // 50, beans_amount // 15]
if min(can_make) > cups:
    print('Yes, I can make that amount of coffee (and even {} more than that)'.format(min(can_make) - cups))
elif min(can_make) == cups:
    print('Yes, I can make that amount of coffee')
elif min(can_make) < cups:
    print('No, I can make only {} cups of coffee'.format(min(can_make)))
time.sleep(2)

print('Starting to make a coffee\n'
      'Grinding coffee beans\n'
      'Boiling water\n'
      'Mixing boiled water with crushed coffee beans\n'
      'Pouring coffee into the cup\n'
      'Pouring some milk into the cup\n'
      'Coffee is ready!')
