import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
j = deque()

for i in range(1,n+1):
    j.append(i)
print(end="<")
for _ in range(n-1):
    for i in range(k-1):
        j.append(j.popleft())
    print(str(j.popleft()),end=", ")
print(j.pop(),end=">")
