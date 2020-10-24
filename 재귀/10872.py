N = int(input())
fact = 1
for i in range(1,N+1):
    fact = fact*i
print(fact)

'''
**for문을 쓰지 않는 경우 (재귀 함수의 이용)

def factorial(num):
    if N == 0:
        return 1
    return N * factorial(N-1)

N = int(input())
print(factorial(N))

'''