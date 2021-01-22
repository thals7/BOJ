import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack += (reversed(graph[vertex])) # 정점이 여러개일 때 정점 번호가 작은 것을 먼저 pop해야하므로 reverse 해준 뒤 stack에 넣어줌 # stack에 vertex의 인접 정점들을 추가할 때 이미 visit한 리스트를 제거하지 않는 이유는 어차피 while문 돌면서 if not in~ 에서 걸러지기 때문
    return visited


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue += graph[vertex]
    return visited


n, m, v = map(int,input().split())
graph = {i:[] for i in range(1,n+1)}

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort() # 입력에서 인접한 정점의 번호가 순서대로 주어지지 않으므로 오름차순으로 정렬해주어야 함

print(' '.join(map(str,(dfs(graph,v)))))
print(' '.join(map(str,(bfs(graph,v)))))