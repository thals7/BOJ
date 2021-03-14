import sys
T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int,sys.stdin.readline().split())
    imp = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    # m의 위치를 저장할 리스트 생성
    order = [0]*n
    order[m] = 1

    while True:
        if imp[0] == max(imp):
            cnt += 1
            if order[0] == 1:
                print(cnt)
                break
            else:
                imp.pop(0)
                order.pop(0)
        else:
            imp.append(imp.pop(0))
            order.append(order.pop(0))
