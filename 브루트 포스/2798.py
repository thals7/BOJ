# 브루트 포스 : 조합 가능한 모든 문자열을 하나씩 대입해 보는 방식으로 암호를 해독하는 방법
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
sum = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if lst[i] + lst[j] + lst[k] > M:
                continue
            else:
                sum = max(sum, lst[i]+lst[j]+lst[k])
print(sum)