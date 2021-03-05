import sys

n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))
p.sort()
time = [p[0]]

for i in range(1,n):
    time.append(time[i-1]+p[i])

print(sum(time))