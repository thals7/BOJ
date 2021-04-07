import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
maps = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
cnt = [[[0]*2 for _ in range(m)] for _ in range(n)]
cnt[0][0][0] = 1

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs():
    queue = deque()
    queue.append((0,0,0))
    while queue:
        x,y,z = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and cnt[nx][ny][z] == 0:
                # 가려는 곳에 벽이 없을 경우
                if maps[nx][ny] == 0:
                    # 벽을 이미 뚫은 배열(cnt[x][y][1])이면 cnt[nx][ny][1]에, 안뚫은 배열(cnt[x][y][0])이면 cnt[nx][ny][0]에 1을 더함
                    cnt[nx][ny][z] = cnt[x][y][z] + 1
                    queue.append((nx,ny,z))
                # 아직 벽을 안뚫었고 가려는 곳에 벽이 있는 경우
                elif z == 0 and maps[nx][ny] == 1:
                    cnt[nx][ny][1] = cnt[x][y][0] + 1
                    queue.append((nx,ny,1))
    return -1

print(bfs())