import sys

n = int(sys.stdin.readline())
stair = [[0] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(9):
        stair[i].append(1)

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            stair[i][j] = stair[i-1][j+1]
        elif j == 9:
            stair[i][j] = stair[i-1][j-1]
        else:
            stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1]

result = stair[n]
print(sum(result) % 1000000000)