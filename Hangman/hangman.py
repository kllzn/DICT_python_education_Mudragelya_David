import random

print(
    'HANGMAN \n'
    'The game will be available soon.'
)

print('HANGMAN')
options = ['python', 'java', 'javascript', 'php']
answer = random.choice(options)
hint = answer[:3]
player_guess = input('Guess the word {}:'.format(hint))
if player_guess == answer:
    print('You survived!')
else:
    print('You lost!')
