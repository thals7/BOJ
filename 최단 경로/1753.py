import sys,heapq

input = lambda : sys.stdin.readline().rstrip()

v,e = map(int, input().split())
k = int(input()) # 시작 정점

graph = {i:set() for i in range(1,v+1)}
for _ in range(e):
    u,v,w = map(int,input().split()) # u: 출발노드 v: 도착노드 w: 가중치
    graph[u].add((v,w))


def dijkstra(graph,start):
    distance = {i:float('inf') for i in graph}
    distance[start] = 0
    Q = [] # 우선순위 큐 생성
    heapq.heappush(Q, (0,start)) # 우선순위 큐에 최초 [d(u),u] 삽입

    while Q:
        # 거리 최소인 노드 선택
        d, u = heapq.heappop(Q)
        for v, w in graph[u]:
            # RELAXATION
            if distance[v] > d + w:
                distance[v] = d + w
                # u의 인접 노드 v를 큐에 삽입
                heapq.heappush(Q, (distance[v],v))

    for i in graph.keys():
        if distance[i] != float('inf'):
            print(distance[i])
        else:
            print('INF')


dijkstra(graph,k)