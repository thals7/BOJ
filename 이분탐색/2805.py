import sys

n, m = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))

left = 0
right = max(tree)
ans = 0

while right >= left:
    mid = (left+right)//2
    tmp = 0
    for t in tree:
        if mid < t:
            tmp += t-mid
    if tmp >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)