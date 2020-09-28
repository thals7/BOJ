while True:
    num = input().split()
    A = int(num[0])
    B = int(num[1])
    if A == 0 and B == 0:
        break
    else:
        print(A+B)