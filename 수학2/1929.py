# 에라토스테네스의 체 이용!

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int,input().split())
for k in range(M, N+1):
    if isPrime(k):
        print(k)