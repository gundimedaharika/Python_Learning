'''
Game where the ball is
'''

from random import shuffle

print('WELCOME TO THE GUESSING GAME')
InitialList = ['_','o','_']
while True:
    Guess = int(input('Please select guess number from 0,1 or 2 : '))
    shuffle(InitialList)
    if (Guess < 0 or Guess > 2):
        print('OUT OF BOUND')
        continue
    else:
        if InitialList[Guess] == 'o':
            print('Congratulations you win the game :')
            print(InitialList)
            break;
        else:
            print('Sorry,Try Again')
            print(InitialList)
            continue
