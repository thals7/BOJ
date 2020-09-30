lst = [int(input()) for i in range(3)]
N = str(lst[0] * lst[1] * lst[2])

for j in range(10):
    cnt = list(N).count(str(j))
    print(cnt)