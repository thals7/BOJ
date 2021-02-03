import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

n,e = map(int,input().split()) # n: 정점의 개수 e: 에지의 개수

# 인접 리스트로 무방향 그래프 구현
graph = {i:set() for i in range(1,n+1)}
for _ in range(e):
    u,v,w = map(int,input().split()) # i,j : 연결된 정점 w : 정점을 잇는 에지의 가중치
    graph[u].add((v,w))
    graph[v].add((u,w))


def prim(graph,start):
    keys = {i:float('inf') for i in graph}
    visited = {i:False for i in graph} # 방문한 노드인지 확인
    total_weight = 0
    keys[start] = 0
    Queue = []
    heapq.heappush(Queue, (keys[start],start)) # 우선순위 큐에 (keys[node],node) 를 삽입

    while Queue:
        key, v = heapq.heappop(Queue)
        if visited[v] == True:
            continue
        visited[v] = True
        total_weight += key
        for u,w in graph[v]:
            if u in keys and w < keys[u]:
                keys[u] = w
                heapq.heappush(Queue, (keys[u],u))

    return total_weight

print(prim(graph,1))
