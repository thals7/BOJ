import sys

input = lambda: sys.stdin.readline().rstrip()
stack = []

k = int(input())

for _ in range(k):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

if len(stack) == 0:
    print(0)
else:
    print(sum(stack))