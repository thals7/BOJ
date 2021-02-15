import sys

input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

num = [i+1 for i in range(n)]
visited = [False] * n
ans = []

def dfs(cnt):
    if cnt == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    for i in range(n):
        if visited[i]:
            continue
        ans.append(num[i])
        visited[i] = [True]

        dfs(cnt+1)

        ans.pop()

        for j in range(i+1,n):
            visited[j] = False

dfs(0)