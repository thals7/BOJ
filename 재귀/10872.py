N = int(input())
fact = 1
for i in range(1,N+1):
    fact = fact*i
print(fact)

'''

**for문을 쓰지 않는 경우 (재귀 함수의 이용)

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

N = int(input())
print(factorial(N))

'''