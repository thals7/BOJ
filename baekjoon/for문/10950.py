t = int(input())
a = [input() for _ in range(t)]
# a = ['1 1', '2 2', '3 3', ...]
for b in range(t):
    c = a[b].split()
    print(int(c[0])+int(c[1]))