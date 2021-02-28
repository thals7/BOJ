import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
dp = [1 for _ in range(n)] # dp[i] = num[i]를 마지막 값으로 가지는 LIS의 길이

for i in range(1,n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))