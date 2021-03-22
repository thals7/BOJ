import sys

a,b,c = map(int,sys.stdin.readline().split())

# 분할 정복을 통해 문제 해결
# 시간 초과
def mul(a,n):
    if n == 1:
        return a

    temp = mul(a,n//2)

    if n % 2 == 0:
        return temp * temp
    else:
        return temp * temp * a

print(mul(a,b)%c)

# 위의 연산에서 매번 % 연산을 함께 수행해줌
# 모듈러 연산의 분배법칙에 의해 (A*B) % C = ((A%C) * (B%C)) % C 가 성립
def mul_res(a,n,c):
    if n == 1:
        return a % c

    temp = mul_res(a, n//2, c)

    if n % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c

print(mul_res(a,b,c))