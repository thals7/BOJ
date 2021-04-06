import sys
from collections import deque
max = 100001

n, k = map(int, sys.stdin.readline().split())
queue = deque()
queue.append(n)
chk = [0]*max
chk[n] = 1

def bfs():
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            chk[cur] = 1
            if cur == k:
                return cnt
            for move in cur-1, cur+1, 2*cur:
                if 0 <= move < max and chk[move] == 0:
                    queue.append(move)
        cnt += 1

print(bfs())