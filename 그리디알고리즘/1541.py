import sys

exp = sys.stdin.readline().rstrip().split('-')
ans = 0

for num in exp[0].split('+'):
    ans += int(num)
for i in exp[1:]:
    for num in i.split('+'):
        ans -= int(num)
print(ans)