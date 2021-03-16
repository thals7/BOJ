import sys

n, m = map(int, sys.stdin.readline().split())
rotate = [i for i in range(1,n+1)]
cnt = 0

for i in map(int, sys.stdin.readline().split()):
    index = rotate.index(i)
    if index <= len(rotate)//2:
        cnt += index
    else:
        cnt += (len(rotate)-index)
    rotate = rotate[index:] + rotate[:index]
    del rotate[0]
print(cnt)