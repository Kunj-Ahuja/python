word = 'Hello World!'
all = 'abcdefghijklmnopqrstuvwxyz'

a = 0

while a < len(word):
    if word[a] == all[a]:
        print(all[a])
    else:
        print(word[a])

    a = a+1