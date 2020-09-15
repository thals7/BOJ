ip = input().split()
a = int(ip[0])
b = int(ip[1])
c = int(ip[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)