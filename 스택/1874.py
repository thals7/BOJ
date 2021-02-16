import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack = []
op = []
cnt = 1

def sequence(cnt):
    for _ in range(n):
        num = int(input())
        while cnt <= num:
            stack.append(cnt)
            op.append("+")
            cnt += 1
        if stack[-1] == num:
            stack.pop()
            op.append("-")
        else:
            print("NO")
            return
    print('\n'.join(op))

sequence(cnt)