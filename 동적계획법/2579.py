import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
stair = [int(input()) for _ in range(n)]
result = [stair[0]]

if n > 1:
    result.append(max(stair[1],stair[0]+stair[1]))
if n > 2:
    result.append(max(stair[0]+stair[2],stair[1]+stair[2]))
    for i in range(3,n):
        temp = max(stair[i]+result[i-2], stair[i]+stair[i-1]+result[i-3])
        result.append(temp)

print(result[n-1])