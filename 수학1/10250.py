T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    Cnt = 0
    for j in range(1,W+1):
        for k in range(1,H+1):
            Cnt += 1
            if Cnt == N:
                break
        else:
            continue
        break
    if j < 10:
        print("{}0{}".format(k,j))
    else:
        print("{}{}".format(k,j))
