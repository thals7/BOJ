import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(n)]
dp2 = [1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if num[i] > num[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

result = 0
for i in range(n):
    tmp = dp[i] + dp2[i] - 1
    if result < tmp:
        result = tmp

print(result)
