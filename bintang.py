A = 20
for m in range (0, A ):
    for n in range (0, A+1):
        print(' ', end='')
    for h in range (0,m+1):
        print('*', end=' ')
    A-=1
    print(' ')