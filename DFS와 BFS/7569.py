import sys
from collections import deque

m, n, h = map(int,sys.stdin.readline().split())
tomato = [list(list(map(int,sys.stdin.readline().split())) for _ in range(n)) for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i,j,k))

def bfs():
    cnt = 0
    dx = [0,1,0,-1,0,0]
    dy = [-1,0,1,0,0,0]
    dz = [0,0,0,0,-1,1]
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            z,y,x = queue.popleft()
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomato[nz][ny][nx] == 0:
                    queue.append((nz,ny,nx))
                    tomato[nz][ny][nx] = 1
    return cnt

def check(cnt):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 0:
                    return -1
    return cnt

print(check(bfs()-1))