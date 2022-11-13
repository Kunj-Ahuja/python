num = int(input('Table of the number: '))
a = 1
print(f'Table of {num}:')
while a<11:
    print(f'{num} x {a} = '+str(a*num))
    a = a + 1