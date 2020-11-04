n = int(input()); x_li = []; y_li = [];
for _ in range(n):
    x, y = map(int,input().split())
    x_li.append(x)
    y_li.append(y)
for i in range(len(x_li)):
    cnt = 1
    for j in range(len(x_li)):
        if x_li[i] < x_li[j] and y_li[i] < y_li[j]: cnt+=1
    print(cnt,end=" ")