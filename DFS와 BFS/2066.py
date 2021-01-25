import sys
input = sys.stdin.readline
print = sys.stdout.write

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex])
    return len(visited)



n = int(input())
pair = int(input())
graph = {i:set() for i in range(1,n+1)}

for _ in range(pair):
    x, y = map(int,input().split())
    graph[x].add(y)
    graph[y].add(x)

print(str(dfs(graph,1)-1))