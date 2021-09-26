bot_name = 'kllzn_bot'
birth_year = '2021'

print('Hello my name is', bot_name)
print('I was created in', birth_year)

print('Please, remind me your name')
your_name = input()
print('What a great name you have, {}!'.format(your_name)) # print('What a great name you have,' + your_name + '!')

print('Let me guess your age')
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print('Your age is {}; that\'s a good time to start programming'.format(your_age))
