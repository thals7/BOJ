import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())


# 1. 재귀 이용 (시간 초과)
def padovan(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n == 4 or n == 5:
        return 2
    else:
        return padovan(n-5) + padovan(n-1)

# 2. for문 + 리스트 이용 (성공)
def padovan(n):
    ans = [1,1,1,2,2]
    if n >= 6:
        for i in range(5,n):
            ans.append(ans[i-5]+ans[i-1])
    return ans[n-1]


for _ in range(T):
    n = int(input())
    print(padovan(n))
