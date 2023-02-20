# Задание №5
# (Simple Fun #261: Whose Move)
# https://www.codewars.com//kata/59126992f9f87fd31600009b

def whoseMove(lastPlayer, win):
    if win == True:
        winner = lastPlayer
    else:
        if lastPlayer == 'white':
            winner = 'black'
        if lastPlayer == 'black':
            winner = 'white'

    return winner