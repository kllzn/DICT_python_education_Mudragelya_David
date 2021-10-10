import time

cups = int(input('Write how many cups of coffee you will need:'))
print('For {} cups of coffee you will need:\n'.format(cups),
      '{} ml of water\n'.format(cups * 200),
      '{} ml of milk\n'.format(cups * 50),
      '{} g of coffee beans'.format((cups * 15)))
time.sleep(1)

print('Starting to make a coffee\n'
      'Grinding coffee beans\n'
      'Boiling water\n'
      'Mixing boiled water with crushed coffee beans\n'
      'Pouring coffee into the cup\n'
      'Pouring some milk into the cup\n'
      'Coffee is ready!')
