import sys, heapq

n = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(heap) == 0:
            sys.stdout.write("0"+"\n")
        else:
            sys.stdout.write(str(heapq.heappop(heap))+"\n")
    else:
        heapq.heappush(heap,x)