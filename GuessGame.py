'''***********************************************
THE GAME IS CALLED GUESSING NUMBER
RULES ARE AS FOLOLWS:
PLAYER SHOULD GUESS THE NUMBER IF GUESS MATCHES
HE WINS THE GAME
AND CODE TELLS HIW MANY GUESSES PLAYER TOOK
HINYTS WILL BE GIVEN TO PLAYER
WHETHER HE/SHE IS NEAR OR FARTHER FRON THE
NUMBER TO GUESS
LETS START THE CODE
************************************************'''

import random
'''GENARATE RANDOM NUMBER BETWEEN 1 AND 100 TO BE GUESSED BY A PLAYER'''
RandomNumberIs = random.randint(1,100)
Guess = 0
Count = 0
PreviousGuess = 0
GuessList = [0]
print('WELCOME TO GUESSING GAME')
print('Guess Number between 1 and 100')
print('If your Guess is more than 10 away from Number, I will print COLD')
print('If your Guess is within 10 from Number, I will print WARM')
print('If your Guess is more away from Previouis Guess, I will print COLDER')
print('If your Guess is Nearer to My Number, I will print WARMER')
while True:
    Guess = int(input('Enter the guess number from 1 to 100 :'))
    print(GuessList)
    print(GuessList[-1])
    if Guess < 1 or Guess > 100:
        print('OUT OF BOUND')
        continue
    if RandomNumberIs == Guess:
        print(f'Congratulations, You guessed in only {len(GuessList)} Guesses')
        break
    if GuessList[-1]:
        if abs(RandomNumberIs - Guess) < abs(GuessList[-1] - RandomNumberIs):
            print('WARMER')
        else:
            print('COLDER')
    else:
        if abs(RandomNumberIs - Guess) <=10:
            print('WARM')
        else:
            print('COLD')
    GuessList.append(Guess)

print('Your GuessList is : ',GuessList)