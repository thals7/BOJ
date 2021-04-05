import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

for _ in range(t):
    l = int(sys.stdin.readline())
    x,y = map(int, sys.stdin.readline().split()) # 현재 나이트가 있는 칸
    m,n = map(int, sys.stdin.readline().split()) # 나이트가 이동하려고 하는 칸

    chk = [[0]*l for _ in range(l)]
    queue = deque()
    queue.append((x,y))
    cnt = 0
    find = False

    chk[x][y] = 1

    while queue:
        for _ in range(len(queue)):
            i,j = queue.popleft()
            if i == m and j == n:
                find = True
                break
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < l and 0 <= ny < l and chk[nx][ny] == 0:
                    queue.append((nx,ny))
                    chk[nx][ny] = 1
        if find:
            break
        cnt += 1

    print(cnt)