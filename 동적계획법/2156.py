import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]
dp = [wine[0]]

if n > 1:
    dp.append(wine[0]+wine[1])
if n > 2:
    dp.append(max(dp[1], wine[1]+wine[2], wine[0]+wine[2]))
if n > 3:
    for i in range(3,n):
        dp.append(max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i]))
        dp[i] = max(dp[i-1], dp[i])

print(max(dp))