bot_name = 'kllzn_bot'
birth_year = '2021'

print('Hello my name is', bot_name)
print('I was created in', birth_year)

print('Please, remind me your name')

your_name = input()

print('What a great name you have, {}!'.format(your_name))  # print('What a great name you have,' + your_name + '!')

print('Let me guess your age')
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print('Your age is {}; that\'s a good time to start programming'.format(your_age))

print('Now I will prove to you that I can count to any number you want.')

your_number = int(input())
i = 0
for i in range(0, your_number + 1):
    print('{}!'.format(i))

print('Completed, have a nice day!')


def test():
    your_answer = input()
    if your_answer == '1':
        print('Completed, have a nice day!')
    else:
        print('Please, try again.')
        test()


print('Let\'s test your programming knowledge.')
print(
    'Why do we go to school? \n'
    '1. For fun \n'
    '2. To  study \n'
    '3. To communicate with other people \n'
    '4. To annoy teachers'
)

test()

print('Congratulations, have a nice day')
