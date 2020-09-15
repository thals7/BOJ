n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j+i<=n:
            print(' ', end='')
        elif j+i>n:
            print('*', end='')
    print()