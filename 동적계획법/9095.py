import sys

T = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(T)]

for n in num:
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    if n == 1:
        print(dp[1])
        continue
    dp[2] = 2
    if n == 2:
        print(dp[2])
        continue
    dp[3] = 4
    if n == 3:
        print(dp[3])
        continue
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])