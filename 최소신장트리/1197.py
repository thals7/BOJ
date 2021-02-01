import sys

input = lambda: sys.stdin.readline().rstrip()

n,e = map(int,input().split()) # n: 정점의 개수 e: 에지의 개수

# 인접 리스트로 그래프 구현
graph = {i:dict() for i in range(1,n+1)}
for _ in range(e):
    i,j,w = map(int,input().split()) # i,j : 연결된 정점 w : 정점을 잇는 에지의 가중치
    graph[i][j] = w
    graph[j][i] = w


def prim(graph,start):
    keys = {}
    pi = {}
    total_weight = 0

    for v in graph.keys():
        keys[v] = float('inf')
        pi[v] = None
    keys[start] = 0

    while keys:
        node, key = min(keys.items(), key =lambda weight:weight[1])
        del keys[node]
        total_weight += key

        for adj, weight in graph[node].items():
            if adj in keys and weight < keys[adj]:
                keys[adj] = weight
                pi[adj] = node

    return total_weight

print(prim(graph,1))