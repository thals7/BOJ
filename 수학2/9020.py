def isPrime(num):
    if num == 1: return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: return False
    return True

lst = list(range(2,10001))
p_lst = []
for i in lst:
    if isPrime(i): p_lst.append(i)

T = int(input())
for _ in range(T):
    n = int(input());p_lst2=[]
    for j in p_lst:
        if j >= n/2: p_lst2.append(j)
    for k in p_lst2:
        if n-k in p_lst:print(n-k, k);break
