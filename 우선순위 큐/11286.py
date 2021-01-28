import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print("0"+"\n")
        else:
            print(str(heapq.heappop(heap)[1])+"\n")
    else:
        heapq.heappush(heap, (abs(x),x))