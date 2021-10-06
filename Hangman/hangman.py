import random

print(
    'HANGMAN \n'
    'The game will be available soon.'
)

print('HANGMAN')
attempts = 8
options = ['python', 'java', 'javascript', 'php']
answer = random.choice(options)
guesses = []
done = False
# wrong_guesses = []
while not done:

    for letter in answer:
        if letter in guesses:
            print(letter, end='')
        else:
            print('_', end='')
    print('')
    guess = input('Input a letter:')

    if guess in guesses:
        attempts -= 1
        print('No improvements')
        # print('Attempts = {}'.format(attempts))
    if guess in answer:
        guesses.append(guess)
    else:
        attempts -= 1
        # wrong_guesses.append(guess)
        print('That letter doesn\'t appear in the word')
        # print('Attempts = {}'.format(attempts))
    if attempts == 0:
        break

    done = True
    for letter in answer:
        if letter not in guesses:
            done = False

if done:
    print('Congrats')
else:
    print('Game over')
