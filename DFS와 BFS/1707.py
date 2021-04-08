import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(start):
    queue = deque()
    queue.append(start)
    chk[start] = 1

    while queue:
        v = queue.popleft()
        for adj in graph[v]:
            # 아직 방문하지 않은 노드인 경우
            if chk[adj] == 0:
                chk[adj] = 3 - chk[v]
                queue.append(adj)
            # 인접한 노드가 이미 방문한 노드이며 색이 같은 경우
            elif chk[adj] == chk[v]:
                return False
    return True


for _ in range(T):
    vertex, edge = map(int,sys.stdin.readline().split())
    graph = {i:set() for i in range(1,vertex+1)}
    chk = [0 for _ in range(vertex+1)]
    ans = True

    for _ in range(edge):
        v1, v2 = map(int,sys.stdin.readline().split())
        graph[v1].add(v2)
        graph[v2].add(v1)

    for i in range(1,vertex+1):
        if chk[i] == 0:
            if not bfs(i):
                ans = False
                break

    print("YES" if ans == True else "NO")