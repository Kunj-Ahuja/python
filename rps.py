import random
from termcolor import  cprint
def win(comp, play):
    cprint('You win!!', 'green')
    cprint(f'You picked {play}, computer picked {comp}', 'blue')

def lose(comp, play):
    cprint('Computer win!!', 'red')
    cprint(f'You picked {play}, computer picked {comp}', 'blue')

def game(comp, play):
    if comp == play:
        cprint('Match tied, both picked ' + comp , 'yellow')
    elif comp == 'rock':
        if play == 'scissor':
            lose(comp, play)
        elif play == 'paper':
            win(comp, play)
    elif comp == 'paper':
        if play == 'rock':
            lose(comp, play)
        elif play == 'scissor':
            win(comp, play)
    elif comp == 'scissor':
        if play == 'paper':
            lose(comp, play)
        elif play == 'rock':
            win(comp, play)

rps = {
    1 : 'rock',
    2 : 'paper',
    3 : 'scissor'
}
def main():
    comp_pick = rps[random.randrange(1,4)]

    player_rps = {
        'r' : 'rock',
        'p' : 'paper',
        's' : 'scissor'
    }

    player_input = input('Choose your pick (r, p, s): ')
    while player_input not in ['r','p','s', 'stop']:
        cprint('Wrong selection!!', 'red')
        player_input = input('Choose your pick (r, p, s): ')
    if player_input == 'stop':
        exit()
    player_pick = player_rps[player_input]

    game(comp_pick, player_pick)

while True:
    main()
    print('------------------------------------------------')