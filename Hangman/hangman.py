import random

# print(
#     'HANGMAN \n'
#     'The game will be available soon.'
# )
print('HANGMAN')


def __menu__():
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        main()
    elif menu == "exit":
        pass
    else:
        __menu__()


def main():

    attempts = 8
    options = ['python', 'java', 'javascript', 'php']
    answer = random.choice(options)
    guesses = []
    done = False
    wrong_guesses = []
    while not done:

        for letter in answer:
            if letter in guesses:
                print(letter, end='')
            else:
                print('_', end='')
        print('')
        guess = input('Input a letter:')
        if len(guess) != 1:
            print('You should input a single letter.')
        elif guess.isupper() is True:
            print('Please enter a lowercase English letter.')
        elif guess in wrong_guesses:
            print('You\'ve already guessed this letter.')
            # print('Attempts = {}'.format(attempts))
        elif guess not in answer:
            attempts -= 1
            wrong_guesses.append(guess)
            print('That letter doesn\'t appear in the word')
            # print('Attempts = {}'.format(attempts))
        elif guess in guesses:
            print('You\'ve already guessed this letter.')
            # print('Attempts = {}'.format(attempts))

        else:
            guesses.append(guess)

        if attempts == 0:
            break

        done = True
        for letter in answer:
            if letter not in guesses:
                done = False

    if done:
        print('You guessed the word {}!'.format(answer))
        print('You survived!')
        __menu__()
    else:
        print('You lost!')
        __menu__()


__menu__()
# возможно код отвратительный, но меня не было на лекции и хорошо, что он вообще работает и главное работает как надо
