import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for _ in range(n):
    i = sys.stdin.readline().split()
    if i[0] == 'push_front':
        deq.appendleft(int(i[1]))
    elif i[0] == 'push_back':
        deq.append(int(i[1]))
    elif i[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif i[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif i[0] == 'size':
        print(len(deq))
    elif i[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif i[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])