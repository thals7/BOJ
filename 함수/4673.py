def d(n):
    lst = list(map(int,str(n)))
    return n + sum(lst)

n_list = []

for i in range(1,10001):
    n_list.append(d(i))
for j in range(1,10001):
    if n_list.count(j) == 0:
        print(j)