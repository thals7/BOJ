import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    stack = []
    ps = list(input())
    ck = 0
    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append(ps[i])
        else:
            if len(stack) == 0 and ps[i] == ")":
                print("NO")
                ck = 1
                break
            else:
                stack.pop()
    if len(stack) == 0 and ck == 0:
        print("YES")
    elif len(stack) != 0 and ck == 0:
        print("NO")