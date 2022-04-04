import os

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
availableMoves = list(theBoard.keys())
usedMoves = []

def printBoard(board):

    os.system('cls||clear')
    
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
def checkWin():
    if theBoard['top-L'] + theBoard['top-M'] + theBoard['top-R'] == 'XXX':
        print('X Wins')
    elif theBoard['mid-L'] + theBoard['mid-M'] + theBoard['mid-R'] == 'XXX':
        print('Win')
    elif theBoard['low-L'] + theBoard['low-M'] + theBoard['low-R'] == 'XXX':
        print('Win')
    elif theBoard['top-L'] + theBoard['mid-L'] + theBoard['low-L'] == 'XXX':
        print('Win')
    elif theBoard['top-M'] + theBoard['mid-M'] + theBoard['low-M'] == 'XXX':
        print('Win')
    elif theBoard['top-R'] + theBoard['mid-R'] + theBoard['low-R'] == 'XXX':
        print('Win')
    elif theBoard['top-L'] + theBoard['mid-M'] + theBoard['low-R'] == 'XXX':
        print('Win')
    elif theBoard['top-R'] + theBoard['mid-M'] + theBoard['low-L'] == 'XXX':
        print('Win')
    elif theBoard['top-L'] + theBoard['top-M'] + theBoard['top-R'] == 'OOO':
        print('Win')
    elif theBoard['mid-L'] + theBoard['mid-M'] + theBoard['mid-R'] == 'OOO':
        print('Win')
    elif theBoard['low-L'] + theBoard['low-M'] + theBoard['low-R'] == 'OOO':
        print('Win')
    elif theBoard['top-L'] + theBoard['mid-L'] + theBoard['low-L'] == 'OOO':
        print('Win')
    elif theBoard['top-M'] + theBoard['mid-M'] + theBoard['low-M'] == 'OOO':
        print('Win')
    elif theBoard['top-R'] + theBoard['mid-R'] + theBoard['low-R'] == 'OOO':
        print('Win')
    elif theBoard['top-L'] + theBoard['mid-M'] + theBoard['low-R'] == 'OOO':
        print('Win')
    elif theBoard['top-R'] + theBoard['mid-M'] + theBoard['low-L'] == 'OOO':
        print('Win')

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    for k in availableMoves:
        print(k, end = ' ')
      
    while True:
        move = input('\nMove: ')
        if len(availableMoves) == 0:
            print('Game Over, No Winner.')
            #
        if move in availableMoves:
            availableMoves.remove(move)
            usedMoves.append(move)
            theBoard[move] = turn
            checkWin()
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            break
        elif move in usedMoves:
            print('Move already used.')
            continue
        else:
            print('Move not found.')
            continue
           
printBoard(theBoard)
