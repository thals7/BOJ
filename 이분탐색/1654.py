import sys

k, n = map(int,(sys.stdin.readline().split()))
lan = [int(sys.stdin.readline()) for _ in range(k)]

left = 1
right = max(lan)

ans = 0

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for l in lan:
        cnt += l//mid
    if cnt >= n:
        if ans < mid:
            ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
