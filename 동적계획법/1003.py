import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())


# 1. 재귀로 구현 (시간초과)
def zero(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return zero(n-1) + zero(n-2)

def one(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return one(n-1) + one(n-2)


for _ in range(T):
    n = int(input())
    print(zero(n), one(n))



# 2. 재귀 없이 for문을 통해 구현 (성공)
for _ in range(T):
    n = int(input())
    zero = 1
    one = 0
    for _ in range(n):
        temp = one
        one = zero + one
        zero = temp
    print(zero, one)



# 3. 결과값을 저장하는 리스트를 만들어 구현 (성공)

for _ in range(T):
    zero = [1,0]
    one = [0,1]
    n = int(input())
    for i in range(2,n+1):
        zero.append(zero[i-2]+zero[i-1])
        one.append(one[i-2]+one[i-1])
    print(zero[n], one[n])