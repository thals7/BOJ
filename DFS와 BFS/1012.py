import sys
sys.setrecursionlimit(10000)

def dfs(y,x):
    cab[y][x] = 0 # visited 한 곳은 1에서 0으로 바꿔줌

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if cab[ny][nx] == 1:
                dfs(ny,nx)


t = int(sys.stdin.readline())
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    cab = [[0 for _ in range(m)] for _ in range(n)]
    ans = 0

    for _ in range(k):
        i,j = map(int,sys.stdin.readline().split())
        cab[j][i] = 1

    for i in range(n):
        for j in range(m):
            if cab[i][j] == 1:
                dfs(i,j)
                ans += 1
    print(ans)