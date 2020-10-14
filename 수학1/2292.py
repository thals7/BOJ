N = int(input())
Cnt = 0
A = 1+6*Cnt
while N > A:
    Cnt += 1
    A = A + 6*Cnt
print(Cnt+1)