import sys

input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

num = [i+1 for i in range(n)]
ans = []

def dfs(cnt):
    if cnt == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    for i in range(n):
        ans.append(num[i])

        dfs(cnt+1)

        ans.pop()

dfs(0)