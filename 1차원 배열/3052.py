N = [int(input()) for _ in range(10)]
N_list = []

for i in N:
    r = int(i)%42
    N_list.append(r)

my_set = set(N_list)
print(len(my_set))