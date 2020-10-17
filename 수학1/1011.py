import math

T = int(input())
for i in range(T):
    x, y = map(int,input().split())
    d = y-x
    n = math.floor(d**0.5)
    if d >= n*(n-1)+1 and d < n*n+1:
        print(n+(n-1))
    elif d >= n*n+1 and d < n*(n+1)+1:
        print(n*2)
    else:
        print(n+(n+1))

