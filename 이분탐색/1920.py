import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
l.sort()

m = int(sys.stdin.readline())
i = list(map(int,sys.stdin.readline().split()))

for num in i:
    left, right = 0, n-1
    ans = 0
    while left <= right:
        mid = (left+right)//2
        if num == l[mid]:
            ans = 1
            break
        elif num > l[mid]:
            left = mid+1
        else:
            right = mid-1
    print(ans)