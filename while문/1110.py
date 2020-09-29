N = input()
if int(N) < 10:
    N = '0'+N
A = N[0]
B = N[-1]
count = 1

while True:
    C = str(int(A)+int(B))[-1]
    New = B+C
    if New == N:
        break
    A = New[0]
    B = New[-1]
    count += 1
print(count)