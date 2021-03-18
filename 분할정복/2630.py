import sys

n = int(sys.stdin.readline())
p = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
cnt = []

# 재귀 이용
def check(x,y,n):
    color = p[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != p[i][j]:
                check(x,y,n//2)
                check(x+n//2,y,n//2)
                check(x,y+n//2,n//2)
                check(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        cnt.append(0)
    else:
        cnt.append(1)

check(0,0,n)
print(cnt.count(0))
print(cnt.count(1))