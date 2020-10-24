import sys; input=sys.stdin.readline
cnt = 0
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    if d == 0:
        if r1==r2: print(-1)
        else: print(0)
    elif d == r1+r2 or d**2 == (r2-r1)**2: print(1)
    elif d < r1+r2 and d**2 > (r2-r1)**2: print(2)
    else: print(0)
