import random

num1 = int(input('Enter the first number of the range: '))
num2 = int(input('Enter the last number of the range: '))

comp_pick = random.randrange(num1,num2)

user_pick = int(input(f'Enter your guess between {num1} - {num2}: '))

if comp_pick == user_pick:
    print('You win!!')
elif comp_pick > user_pick:
    print(f'Computer pick is greater than yours by {comp_pick - user_pick} : {comp_pick}')
else:
    print(f'Computer pick is smaller than yours by {user_pick - comp_pick} : {comp_pick}')