import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input()); m = int(input())


graph = [[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i,j,w = map(int,input().split())
    graph[i][j] = min(graph[i][j], w)


def floydWarshall(graph):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] == float('inf'):
                print(0,end=' ')
            else:
                print(graph[i][j],end=' ')
        print()

floydWarshall(graph)