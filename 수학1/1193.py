X = int(input())
N = 1
Cnt = 0
while X >= N:
    Cnt += 1
    N = N + Cnt
N = N - Cnt
if Cnt%2 == 0:
    A = 1
    B = Cnt
    while X != N:
        N += 1
        A += 1
        B -= 1
else:
    A = Cnt
    B = 1
    while X != N:
        N += 1
        A -= 1
        B += 1
print("{}/{}".format(A,B))