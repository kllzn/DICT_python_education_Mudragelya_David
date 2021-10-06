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

while not done:

    for letter in answer:
        if letter in guesses:
            print(letter, end='')
        else:
            print('_', end='')
    print('')

    guess = input('Input a letter:')
    guesses.append(guess)
    attempts -= 1
    if guess not in answer:
        print('That letter doesn\'t appear in the word')
        if attempts == 0:
            break

    done = True
    for letter in answer:
        if letter not in guesses:
            done = False

# if done:
#     print('Congrats')
# else:
#     print('Game over')
print('Thanks for playing!\nWe\'ll see how well you did in the next stage')
