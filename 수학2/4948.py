def isPrime(num):
    if num == 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

lst = list(range(2,246912))
p_lst = []
for i in lst:
    if isPrime(i):
        p_lst.append(i)

while True:
    n = int(input());cnt=0
    if n == 0: break
    for i in p_lst:
        if n < i <= n*2:
            cnt += 1
    print(cnt)