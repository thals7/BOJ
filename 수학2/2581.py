import math
M=int(input());N=int(input());lst=[]
for i in range(M,N+1):
    Cnt = 0
    if i == 1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            Cnt += 1
            break
    if Cnt == 0:
        lst.append(i)
if not lst:
    print(-1)
else:
    print(sum(lst),min(lst), sep='\n')