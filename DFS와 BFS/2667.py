import sys
input = lambda: sys.stdin.readline().rstrip()


def dfs(x,y):
    cnt = 1
    # 방문한 곳을 1에서 0으로 바꿔줌(중복 방문 방지하기 위해)
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배열 범위 벗어나지 않았는지 확인
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 1:
                cnt += dfs(nx,ny)
    return cnt


n = int(input()); result = []
graph = [list(map(int,input())) for _ in range(n)]
# 좌표 문제에서 리스트를 만들어 접근할 경우 깔끔한 풀이 가능
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs(i,j))
print(len(result))
print("\n".join(map(str,sorted(result))))