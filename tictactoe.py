from termcolor import colored,cprint
def print_board(p1,p2):
    one =  colored('X', 'red') if '1' in p1 else (colored('O', 'blue') if ('1' in p2) else '1')
    two =  colored('X', 'red') if '2' in p1 else (colored('O', 'blue') if ('2' in p2) else '2')
    three =  colored('X', 'red') if '3' in p1 else (colored('O', 'blue') if ('3' in p2) else '3')
    four =  colored('X', 'red') if '4' in p1 else (colored('O', 'blue') if ('4' in p2) else '4')
    five =  colored('X', 'red') if '5' in p1 else (colored('O', 'blue') if ('5' in p2) else '5')
    six =  colored('X', 'red') if '6' in p1 else (colored('O', 'blue') if ('6' in p2) else '6')
    seven =  colored('X', 'red') if '7' in p1 else (colored('O', 'blue') if ('7' in p2) else '7')
    eight =  colored('X', 'red') if '8' in p1 else (colored('O', 'blue') if ('8' in p2) else '8')
    nine =  colored('X', 'red') if '9' in p1 else (colored('O', 'blue') if ('9' in p2) else '9')
    print(f'{one} | {two} | {three}')
    print('---------')
    print(f'{four} | {five} | {six}')
    print('---------')
    print(f'{seven} | {eight} | {nine}')

def check_wins(p1,p2):
    wins = [['1','2','3'], ['1','4','7'],['1','5','9'],['2','5','8'],['3','6','9'],['3','5','7'],['4','5','6'],['7','8','9']]
    if any(set(win).issubset(p1) for win in wins):
        cprint('X : Wins', 'red')
        exit()
    elif any(set(win).issubset(p2) for win in wins):
        cprint('O : Wins', 'blue')
        exit()
    else: return
p1Data = []
p2Data = []
print_board(p1Data,p2Data)
def input_p():

    p1 = input(colored('X : Enter your position: ', 'red'))
    mix = p1Data+p2Data
    while p1 in mix:
        print('Invalid move!')
        p1 = input(colored('X : Enter your position: ', 'red'))
        p1Data.append(p1)
    p1Data.append(p1)
    print_board(p1Data,p2Data)
    check_wins(p1Data,p2Data)
    cprint('--------------', 'yellow')


    mix = p1Data+p2Data
    p2 = input(colored('O : Enter your position: ', 'blue'))
    while p2 in mix:
        print('Invalid move!')
        p2 = input(colored('O : Enter your position: ', 'blue'))
        p2Data.append(p2)
    p2Data.append(p2)
    print_board(p1Data,p2Data)
    check_wins(p1Data,p2Data)
    cprint('--------------', 'yellow')


while len(p1Data) + len(p2Data) < 9:
    input_p()

while len(p1Data) + len(p2Data) == 9:
    print('Draw')