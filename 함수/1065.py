import sys

n = int(sys.stdin.readline())
cnt = 0

if n > 99:
    cnt = 99
    for i in range(100,n+1):
        num = list(map(int,list(str(i))))
        isSeq = True
        tmp = num[-1]-num[-2]
        for j in range(len(num)-1,0,-1):
            if tmp == num[j]-num[j-1]:
                continue
            else:
                isSeq = False
                break
        if isSeq:
            cnt += 1
else:
    cnt = n

print(cnt)