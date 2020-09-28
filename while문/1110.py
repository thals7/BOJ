N = input()
A = int(N[0])
B = int(N[-1])
count = 1
while True:
    C = A+B
    if C == int(N):
        break
    D = str(C)
    A = B
    B = int(D[-1])
    count += 1

print(count)