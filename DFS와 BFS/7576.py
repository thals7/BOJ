import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())
tomato = [list(map(int,list(sys.stdin.readline().split()))) for _ in range(n)]
result = 0
queue = deque()

dy = [-1,0,1,0]
dx = [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i,j))

while queue:
    result += 1
    for _ in range(len(queue)):
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and tomato[ny][nx] == 0:
                queue.append((ny,nx))
                tomato[ny][nx] = 1

def check():
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return -1
    return result-1

print(check())