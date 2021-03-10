import sys

n = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))
cost = 0
min = price[0]

for i in range(n-1):
    if min > price[i]:
        min = price[i]
    cost += min*road[i]

print(cost)