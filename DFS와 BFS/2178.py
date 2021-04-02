import sys

n, m = map(int,sys.stdin.readline().split())

maze = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
maze[0][0] = 0
queue = [(0,0)]
chk = [[0]*m for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

while queue:
    y,x = queue.pop(0)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 1:
            queue.append((ny,nx))
            chk[ny][nx] = chk[y][x]+1
            maze[ny][nx] = 0

print(chk[n-1][m-1]+1)