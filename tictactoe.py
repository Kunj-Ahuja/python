from termcolor import colored,cprint

def ttt():
    x_wins = 0
    o_wins = 0
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

    
    def score_board(x,o):
        print(f'''Wins ->
        ---------
        | X | O |
        ---------
        | {x} | {o} | 
        ---------
        ''')
        if input('Wanna one more game (Y/N): ') == 'Y':
            ttt()
        else:
            exit()
        
    
    def check_wins(p1,p2):
        
        wins = [['1','2','3'], ['1','4','7'],['1','5','9'],['2','5','8'],['3','6','9'],['3','5','7'],['4','5','6'],['7','8','9']]
        if any(set(win).issubset(p1) for win in wins):
            cprint('X : Wins', 'red')
            x_wins = x_wins+1
            score_board(x_wins,o_wins)
        elif any(set(win).issubset(p2) for win in wins):
            cprint('O : Wins', 'blue')
            o_wins = o_wins+1
            score_board(x_wins,o_wins)
        else: return

    p1Data = []
    p2Data = []
    print_board(p1Data,p2Data)

    def input_p():

        p1 = input(colored('X : Enter your position: ', 'red'))
        mix = p1Data+p2Data
        if p1 == '':
            print('Invalid move!')
            p1 = input(colored('X : Enter your position: ', 'red'))
            p1Data.append(p1)
        while p1 in mix:
            print('Invalid move!')
            p1 = input(colored('X : Enter your position: ', 'red'))
            p1Data.append(p1)
        p1Data.append(p1)
        print_board(p1Data,p2Data)
        check_wins(p1Data,p2Data)
        cprint('--------------', 'yellow')
        if len(p1Data) + len(p2Data) == 9:
            print('Draw')  
        mix = p1Data+p2Data
        p2 = input(colored('O : Enter your position: ', 'blue'))
        if p2 == '':
            print('Invalid move!')
            p2 = input(colored('O : Enter your position: ', 'blue'))
            p2Data.append(p2)
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

while True:
    ttt()