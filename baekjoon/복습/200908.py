#11022
import sys
t = int(sys.stdin.readline())
for i in range(t):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d' %(i+1,A,B,A+B))

#2438
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*', end='')
    print()

#10871
n, x = map(int, input().split())
a = input().split()
for i in range(n):
    if int(a[i]) < x:
        print(a[i], end=" ")

#10871-2
n, x = map(int, input().split())
a = []
b = list(map(int, input().split()))
for i in b:
    if i < x:
        a.append(str(i))
print(' '.join(a))