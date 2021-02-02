import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = {i:set() for i in range(1, n + 1)}
for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x].add((y,w))


def bellmanFord(graph,start):
    distance = {}
    pi = {}
    for vertex in graph:
        distance[vertex] = float('inf')
        pi[vertex] = None
    distance[start] = 0

    for _ in range(len(graph)):
        for u in graph:
            # RELAXATION
            for v,w in graph[u]:
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    pi[v] = u

    for u in graph:
        for v,w in graph[u]:
            if distance[v] > distance[u] + w:
                print(-1)
                return

    for d in range(2,len(distance)+1):
        if distance[d] != float('inf'):
            print(distance[d])
        else:
            print(-1)

bellmanFord(graph,1)