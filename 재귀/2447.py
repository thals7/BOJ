import sys

n = int(sys.stdin.readline())
stars = [[' ']*n for _ in range(n)]

def star(x, y, n):
    if n == 1:
        stars[x][y] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                star(x+(n//3)*i, y+(n//3)*j, n//3)
    return

star(0,0,n)

for i in range(n):
    print(''.join(stars[i]))