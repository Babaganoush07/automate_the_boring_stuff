import random
import sys
count = 0
while True:
    ran_dom = (random.randint(1, 5))
    guess = input("Guess the number between (1-5): ")

    try:
        int(guess)
    except ValueError:
        print('Please enter whole numbers only.')
        continue
    if int(guess) < 1 or int(guess) > 5:
        print('Out of range, Guess between 1 and 5.')
        continue
    elif int(guess) != int(ran_dom):
        print('Wrong. The number was: ' + str(ran_dom))
        count += 1
        if count == 10:
            print('Really? ' + str(count) + ' guesses?')
        elif count == 15:
            print('Wow! ' + str(count) + ' guesses?')
        elif count == 20:
            print('This is just sad. ' + str(count) + ' guesses?')
        elif count == 30:
            print('Please, Just stop. ' + str(count) + ' guesses?')
        continue
    elif int(guess) == int(ran_dom):
        count += 1
        print('You guessed it! After ' + str(count) + ' guesses.')
        count = 0

        while True:
            play_again = input('Play again? Y / N: ')
            if play_again == 'Y' or play_again == 'y':
                break
            elif play_again == 'N' or play_again == 'n':
                print('Game over.')
                sys.exit()
            elif play_again != 'Y' or play_again != 'N':
                print('Please enter Y or N.')
                continue

