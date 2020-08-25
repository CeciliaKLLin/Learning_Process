from random import randint
import sys


def guessing_game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are right!')
            return True
    else:
        print('hey, 1~10')
        return False

answer = randint(int(1), int(10))
#answer = randint(int(sys.argv[1]), int(sys.argv[2]))
if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number 1-10:'))
            if guessing_game(guess, answer):
               break
        except ValueError:
            print('Please enter a number')
            continue



