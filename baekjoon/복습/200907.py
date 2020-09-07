#15552
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


#11022
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d'%(i+1,a,b,a+b))

#2438
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*',end='')
    print()