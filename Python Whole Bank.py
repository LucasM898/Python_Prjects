import os
with open('bob.txt', 'r') as file:
    if os.path.isfile('bob.txt'):
        print(file.readline())
    else:
        print('nofile')
