import sys

n, k = map(int,sys.stdin.readline().split())
coin = list(int(sys.stdin.readline()) for _ in range(n))
total = 0

for i in reversed(coin):
    total += k//i
    k %= i
print(total)