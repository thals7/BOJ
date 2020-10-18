N = int(input())
N_lst = list(map(int,input().split()))
Cnt = 0
for i in N_lst:
    if i == 1:
        Cnt += 1
    else:
        for j in range(2,i):
            if i/j == i//j:
                Cnt += 1
                break
            else:
                continue
print(N-Cnt)

# 비효율적인 방법. 숫자가 커질수록 걸리는 시간 커짐
# 가장 효율적인 방법은? 숫자의 N**0.5(루트N)까지 확인하는 방법