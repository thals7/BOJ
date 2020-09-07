n, x = map(int, input().split())
l = input().split()
for i in range(n):
    a = l[i]
    if int(a)<x:
        print(int(a), end=' ')