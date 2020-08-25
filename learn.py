from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
while True:
    try:
        guess = int(input('guess a number 1-10:'))
        if 0 < guess < 11:
            if guess == answer:
                print('you are right!')
                break
        else:
            print('hey, 1~10')
    except ValueError:
        print('Please enter a number')
        continue
