import sys

n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

dicts = dict()

for i in card:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1

for i in num:
    if i in dicts:
        print(dicts[i], end=" ")
    else:
        print(0, end =" ")