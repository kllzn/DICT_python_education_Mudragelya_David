import random

print(
    'HANGMAN \n'
    'The game will be available soon.'
)

print('HANGMAN')
options = ['python', 'java', 'javascript', 'php']
answer = random.choice(options)
answer1 = answer[:3] + '-' * (len(answer)-3)

player_guess = input('Guess the word {}:'.format(answer1))
if player_guess == answer:
    print('You survived!')
else:
    print('You lost!')
