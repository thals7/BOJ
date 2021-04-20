import sys

m1 = []
m2 = []

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    m1.append(list(map(int,sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())
for _ in range(m):
    m2.append(list(map(int,sys.stdin.readline().split())))

result = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += m1[i][l] * m2[l][j]

for lst in result:
    print(' '.join(map(str,lst)))