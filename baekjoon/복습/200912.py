#2439
import sys
input = sys.stdin.readline

n = int(input())
for i in range(1,n+1):
    for j in range(n):
        if n-i <= j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#10871
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = input().split()
list = []
for i in range(n):
    if int(a[i]) < x:
        list.append(a[i])
print(' '.join(list))