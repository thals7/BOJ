t = input().split()
h = int(t[0])
m = int(t[1])

if m>=45:
    print(h, m-45)
elif m<45 and h==0:
    print(h+23, m+15)
else: print(h-1, m+15)